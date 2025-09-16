import re
from pathlib import Path
from typing import Dict, List, Tuple

REPO_ROOT = Path(__file__).resolve().parents[1]
SOPS_DIR = REPO_ROOT / "sops"
OUTPUT_DIR = REPO_ROOT / "lesson-plans"

OUTPUT_DIR.mkdir(exist_ok=True)

SectionMap = Dict[str, List[str]]


def cleanup_heading(raw: str) -> str:
    text = raw.strip()
    text = text.lstrip('#').strip()
    if text.startswith('**') and text.endswith('**') and len(text) >= 4:
        text = text[2:-2]
    text = text.replace('\\', '')
    text = re.sub(r'^\d+(\.\d+)*\s*', '', text)
    return text.strip()


def strip_markdown(text: str) -> str:
    return re.sub(r'[*_`]', '', text)


def extract_sections(lines: List[str]) -> SectionMap:
    sections: SectionMap = {}
    current = None
    buffer: List[str] = []

    for line in lines:
        if line.strip().startswith('##'):
            if current is not None:
                sections[current] = buffer
            current = cleanup_heading(line)
            buffer = []
        else:
            if current is not None:
                buffer.append(line.rstrip('\n'))
    if current is not None:
        sections[current] = buffer
    return sections


def find_section(sections: SectionMap, *keywords: str) -> List[str]:
    for key, value in sections.items():
        lower = key.lower()
        for keyword in keywords:
            if keyword.lower() in lower:
                return value
    return []


def parse_title(lines: List[str], fallback: str) -> str:
    for line in lines:
        plain = line.replace('*', '')
        match = re.search(r'\btitle\b[:：]\s*(.*)', plain, flags=re.IGNORECASE)
        if match:
            title = match.group(1).strip()
            return title if title else fallback
    # look for first markdown heading
    for line in lines:
        if line.startswith('#'):
            title = cleanup_heading(line)
            return title if title else fallback
    return fallback


def clean_text(cell: str) -> str:
    text = cell.replace('**', '')
    text = text.replace('\\-', '-')
    text = text.replace('\\&', '&')
    text = text.replace('\\', '')
    text = text.replace('\n', ' ')
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def parse_table(lines: List[str]) -> List[Tuple[str, str]]:
    entries: List[Tuple[str, str]] = []
    for raw in lines:
        line = raw.strip()
        if not line.startswith('|'):
            continue
        cells = [c.strip() for c in line.strip('|').split('|')]
        if len(cells) < 2:
            continue
        first, second = cells[0], cells[1]
        if not first or set(first) <= {'-', ' '}:
            continue
        header_tokens = {'term', 'role', 'responsibilities', 'definition'}
        if first.lower() in header_tokens or second.lower() in header_tokens:
            continue
        entries.append((clean_text(first), clean_text(second)))
    return entries


def format_responsibilities(text: str) -> str:
    cleaned = clean_text(text)
    if not cleaned:
        return cleaned
    if cleaned.startswith('-'):
        parts = [part.strip() for part in re.split(r'-\s+', cleaned) if part.strip()]
        if parts:
            normalized = [part.rstrip(';.') for part in parts]
            joined = '; '.join(normalized)
            if cleaned.endswith('.'):
                joined += '.'
            return joined
    return cleaned


def format_list(items: List[str]) -> str:
    if not items:
        return ''
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return f"{items[0]} and {items[1]}"
    return ', '.join(items[:-1]) + f", and {items[-1]}"


def restructure_scope_line(line: str, default_prefix: str) -> str:
    text = re.sub(r'^[*-]\s*', '', line.strip())
    text = text.replace('\\', '')
    text = re.sub(r'\s+', ' ', text)
    text = text.rstrip(':.')
    trailing_phrases = [' including', ' including but not limited to', ' including without limitation', ' it encompasses']
    lowered = text.lower()
    for phrase in trailing_phrases:
        if lowered.endswith(phrase):
            text = text[: -len(phrase)]
            break
    text = re.sub(r',\s*$', '', text)
    replacements = [
        ('This SOP covers', 'Covers'),
        ('This procedure covers', 'Covers'),
        ('This policy covers', 'Covers'),
        ('This SOP includes', 'Includes'),
        ('This SOP encompasses', 'Encompasses'),
        ('The scope includes', 'Includes'),
        ('Scope includes', 'Includes'),
        ('This SOP applies to', 'Applies to'),
        ('This procedure applies to', 'Applies to'),
        ('This policy applies to', 'Applies to'),
        ('It applies to', 'Applies to'),
        ('Applies to', 'Applies to'),
        ('Applicable to', 'Applies to'),
        ('The scope applies to', 'Applies to'),
    ]
    lowered = text.lower()
    for old, new in replacements:
        if lowered.startswith(old.lower()):
            text = new + text[len(old):]
            break
    else:
        if default_prefix and not re.match(r'^(covers|includes|addresses|outlines|focuses|guides|defines|encompasses|applies|sets)', lowered):
            text = default_prefix + text
    text = re.sub(r'^(Covers|Includes|Applies to|Addresses|Focuses on|Guides|Defines|Encompasses):\s*', r'\1 ', text)
    text = text.rstrip('.')
    text = text.strip()
    if text:
        text = text[0].upper() + text[1:]
    return text + '.' if text else ''


def summarize_scope(lines: List[str]) -> str:
    entries: List[Tuple[str, bool]] = []
    for raw in lines:
        stripped = raw.strip()
        if not stripped:
            continue
        is_bullet = bool(re.match(r'^[*-]', stripped))
        without_marker = re.sub(r'^[*-]\s*', '', stripped)
        cleaned = strip_markdown(without_marker)
        if cleaned and not set(cleaned) <= {'-', ' '}:
            entries.append((cleaned, is_bullet))

    if not entries:
        return 'Scope details not provided.'

    phase_names: List[str] = []
    for cleaned, is_bullet in entries:
        if is_bullet:
            match = re.match(r'([^:]+):', cleaned)
            if match:
                phase = match.group(1).strip()
                if phase and phase not in phase_names:
                    phase_names.append(phase)

    non_bullet = [cleaned for cleaned, is_bullet in entries if not is_bullet]

    cover_line = None
    for line in non_bullet:
        lowered = line.lower()
        if any(keyword in lowered for keyword in ['scope', 'cover', 'encompass', 'include', 'govern', 'guide', 'appl']):
            cover_line = line
            break
    if cover_line is None:
        cover_line = non_bullet[0] if non_bullet else entries[0][0]

    applies_line = None
    for line in non_bullet:
        if line == cover_line:
            continue
        lowered = line.lower()
        if any(keyword in lowered for keyword in ['appl', 'team', 'stakeholder', 'audience', 'personnel', 'department', 'group']):
            applies_line = line
    if applies_line is None and len(non_bullet) > 1:
        candidate = non_bullet[-1]
        if candidate != cover_line:
            applies_line = candidate

    sentences: List[str] = []
    if cover_line:
        sentences.append(restructure_scope_line(cover_line, 'Covers '))
    if phase_names:
        sentences.append(f"Includes focus areas such as {format_list(phase_names)}.")
    if applies_line:
        applies_sentence = restructure_scope_line(applies_line, '')
        if applies_sentence:
            sentences.append(applies_sentence)

    return ' '.join(sentences) if sentences else 'Scope details not provided.'


def write_lesson_plan(sop_path: Path) -> None:
    lines = sop_path.read_text(encoding='utf-8').splitlines()
    sections = extract_sections(lines)
    objective_lines = find_section(sections, 'objective', 'purpose')
    scope_lines = find_section(sections, 'scope')
    definitions_lines = find_section(sections, 'definition')
    roles_lines = find_section(sections, 'role')

    title = parse_title(lines, sop_path.stem)

    output_path = OUTPUT_DIR / f"{sop_path.stem}-lesson-plan.md"
    with output_path.open('w', encoding='utf-8') as fh:
        fh.write(f"# Lesson Plan Draft: {title}\n\n")
        fh.write(f"**SOP Reference:** {sop_path.stem}\n\n")

        fh.write("## Objective\n\n")
        if objective_lines:
            filtered_objective = [line for line in objective_lines if line.strip() not in {'---', '***'}]
            fh.write('\n'.join(filtered_objective).strip() + '\n\n')
        else:
            fh.write("Objective details not provided in the SOP.\n\n")

        fh.write("## Audience & Applicability\n\n")
        fh.write(summarize_scope(scope_lines) + "\n\n")

        fh.write("## Key Definitions\n\n")
        definitions = parse_table(definitions_lines)
        if definitions:
            for term, definition in definitions:
                fh.write(f"- **{term}**: {definition}\n")
            fh.write("\n")
        else:
            fh.write("- No key definitions provided.\n\n")

        fh.write("## Key Roles\n\n")
        roles = parse_table(roles_lines)
        if roles:
            for role, responsibilities in roles:
                fh.write(f"- **{role}**: {format_responsibilities(responsibilities)}\n")
            fh.write("\n")
        else:
            fh.write("- No roles and responsibilities provided.\n")


def main() -> None:
    sop_files = sorted(p for p in SOPS_DIR.glob('SOP-[0-9]*.md'))
    if not sop_files:
        raise SystemExit('No SOP files found.')
    for path in sop_files:
        write_lesson_plan(path)


if __name__ == '__main__':
    main()
