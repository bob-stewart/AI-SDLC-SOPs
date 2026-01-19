import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple

ROOT = Path(__file__).resolve().parent.parent
SOPS_DIR = ROOT / "sops"
OUTPUT_DIR = ROOT / "lessons"


@dataclass
class TextSpan:
    text: str
    start: int
    end: int


def read_lines(path: Path) -> List[str]:
    return path.read_text(encoding="utf-8").splitlines()


def section_indices(lines: List[str]) -> Dict[str, Tuple[int, int]]:
    pattern_hash = re.compile(r"^##+\s+\*\*(.+?)\*\*")
    pattern_star = re.compile(r"^\*\*(\d+(?:\.\d+)*)(?:\.)?\s+(.+?)\*\*")
    indices: Dict[str, Tuple[int, int]] = {}
    headings: List[Tuple[str, int, int]] = []
    for idx, line in enumerate(lines):
        stripped = line.strip()
        normalized = stripped.replace("\\.", ".")
        match_hash = pattern_hash.match(normalized)
        if match_hash:
            level = normalized.count("#", 0, normalized.find(" "))
            headings.append((match_hash.group(1).strip(), idx, level))
            continue
        match_star = pattern_star.match(normalized)
        if match_star:
            title = f"{match_star.group(1)} {match_star.group(2).strip()}"
            level = 2 + match_star.group(1).count(".")
            headings.append((title, idx, level))
    for i, (title, start, level) in enumerate(headings):
        end = len(lines)
        for _next_title, next_start, next_level in headings[i + 1 :]:
            if next_level <= level:
                end = next_start
                break
        indices[title] = (start, end)
    return indices


def section_slice(lines: List[str], indices: Dict[str, Tuple[int, int]], title_keywords: List[str]) -> List[Tuple[int, str]]:
    for keyword in title_keywords:
        for title, (start, end) in indices.items():
            if keyword.lower() in title.lower():
                return [(idx + 1, lines[idx]) for idx in range(start + 1, end)]
    return []


def extract_paragraph(section_lines: List[Tuple[int, str]]) -> Optional[TextSpan]:
    buffer: List[str] = []
    start_line = None
    for line_no, line in section_lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("---"):
            if buffer:
                break
            continue
        if stripped.startswith(("|", "- ", "* ", "1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "9.", "##")):
            if buffer:
                break
            continue
        if start_line is None:
            start_line = line_no
        buffer.append(stripped)
    if buffer and start_line is not None:
        end_line = start_line + len(buffer) - 1
        text = " ".join(buffer)
        return TextSpan(text=text, start=start_line, end=end_line)
    return None


def collect_numbered_items(section_lines: List[Tuple[int, str]]) -> List[TextSpan]:
    items: List[TextSpan] = []
    current_lines: List[str] = []
    start_line: Optional[int] = None
    for line_no, line in section_lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("---"):
            if current_lines and start_line is not None:
                text = " ".join(current_lines)
                end_line = start_line + len(current_lines) - 1
                items.append(TextSpan(text=text, start=start_line, end=end_line))
                current_lines = []
                start_line = None
            continue
        if re.match(r"^\d+\.\s", stripped):
            if current_lines and start_line is not None:
                text = " ".join(current_lines)
                end_line = start_line + len(current_lines) - 1
                items.append(TextSpan(text=text, start=start_line, end=end_line))
            content = stripped.split(" ", 1)[1] if " " in stripped else stripped
            current_lines = [content]
            start_line = line_no
        elif stripped.startswith("*") or stripped.startswith("-"):
            if current_lines:
                cleaned = re.sub(r"^[*-]\s*", "", stripped)
                cleaned = cleaned.replace("*", "")
                current_lines.append(cleaned)
        elif stripped and start_line is not None:
            current_lines.append(stripped)
    if current_lines and start_line is not None:
        text = " ".join(current_lines)
        end_line = start_line + len(current_lines) - 1
        items.append(TextSpan(text=text, start=start_line, end=end_line))
    return items


def collect_subheadings(section_lines: List[Tuple[int, str]]) -> List[TextSpan]:
    spans: List[TextSpan] = []
    pattern_hash = re.compile(r"^###\s+\*\*(.+?)\*\*")
    pattern_star = re.compile(r"^\*\*(\d+\.\d+[^*]*)\*\*")
    for line_no, line in section_lines:
        match_hash = pattern_hash.match(line)
        if match_hash:
            spans.append(TextSpan(match_hash.group(1).strip(), line_no, line_no))
            continue
        match_star = pattern_star.match(line)
        if match_star:
            spans.append(TextSpan(match_star.group(1).strip(), line_no, line_no))
    return spans


def collect_step_blocks(section_lines: List[Tuple[int, str]]) -> List[TextSpan]:
    blocks: List[TextSpan] = []
    i = 0
    while i < len(section_lines):
        line_no, line = section_lines[i]
        stripped = line.strip()
        if not stripped or stripped.startswith("---"):
            i += 1
            continue
        match = re.match(r"^(\d+)\.\s*(.+?)\s*:?$", stripped)
        bold_match = re.match(r"^\*\*(.+?)\*\*\s*:?\s*(.*)$", stripped)
        if match:
            description = match.group(2)
            block_lines = [description]
            start_line = line_no
            j = i + 1
            end_line = line_no
            while j < len(section_lines):
                next_line_no, next_line = section_lines[j]
                next_stripped = next_line.strip()
                if not next_stripped:
                    j += 1
                    continue
                if next_stripped.startswith("---") or re.match(r"^\d+\.\s", next_stripped) or next_stripped.startswith("###"):
                    break
                cleaned = re.sub(r"^[*-]\s*", "", next_stripped)
                cleaned = re.sub(r"\*\*(.+?)\*\*", r"\1", cleaned)
                cleaned = cleaned.replace("*", "")
                block_lines.append(cleaned)
                end_line = next_line_no
                j += 1
            text = " — ".join(block_lines)
            blocks.append(TextSpan(text=text, start=start_line, end=end_line))
            i = j
        elif bold_match and bold_match.group(1).strip():
            title = bold_match.group(1).strip()
            first_token = title.split()[0] if title.split() else ""
            if re.fullmatch(r"\d+(?:\.\d+)*", first_token):
                i += 1
                continue
            remainder = bold_match.group(2).strip()
            block_lines = [f"{title}{(': ' + remainder) if remainder else ''}"]
            start_line = line_no
            end_line = line_no
            j = i + 1
            while j < len(section_lines):
                next_line_no, next_line = section_lines[j]
                next_stripped = next_line.strip()
                if not next_stripped:
                    j += 1
                    continue
                if next_stripped.startswith("---") or re.match(r"^\d+\.\s", next_stripped) or re.match(r"^\*\*\d", next_stripped):
                    break
                if re.match(r"^\*\*(.+?)\*\*", next_stripped):
                    break
                cleaned = re.sub(r"^[*-]\s*", "", next_stripped)
                cleaned = re.sub(r"\*\*(.+?)\*\*", r"\1", cleaned)
                cleaned = cleaned.replace("*", "")
                block_lines.append(cleaned)
                end_line = next_line_no
                j += 1
            text = " — ".join(block_lines)
            blocks.append(TextSpan(text=text, start=start_line, end=end_line))
            i = j
        else:
            i += 1
    return blocks


def collect_deliverables(section_lines: List[Tuple[int, str]]) -> List[TextSpan]:
    spans: List[TextSpan] = []
    pattern = re.compile(r"\*\s*\*?Deliverables\*?\s*:?\s*(.+)")
    for line_no, line in section_lines:
        match = pattern.search(line)
        if match:
            text = match.group(1).strip().lstrip("*").strip().replace("*", "")
            if text:
                spans.append(TextSpan(text, line_no, line_no))
    return spans


def collect_roles(section_lines: List[Tuple[int, str]]) -> List[Tuple[str, TextSpan]]:
    rows: List[Tuple[str, TextSpan]] = []
    for line_no, line in section_lines:
        stripped = line.strip()
        if stripped.startswith("|") and "Responsibilities" not in stripped and not stripped.startswith("| -----"):
            parts = [part.strip() for part in stripped.strip("|").split("|")]
            if len(parts) >= 2 and parts[0] and parts[1]:
                if parts[0].lower() == "role" and parts[1].lower().startswith("responsibility"):
                    continue
                rows.append((parts[0], TextSpan(parts[1], line_no, line_no)))
    return rows


def classify_raci(text: str) -> Tuple[bool, bool, bool, bool]:
    lower = text.lower()
    responsible = True
    accountable = any(
        keyword in lower
        for keyword in [
            "final authority",
            "approves",
            "approval",
            "sign-off",
            "issues formal approval",
            "provides final decisions",
            "champions",
            "final decisions",
            "final approval",
        ]
    )
    consulted = any(
        keyword in lower
        for keyword in [
            "consult",
            "coordinate",
            "coordinates",
            "collabor",
            "engages",
            "reviews with",
            "works with",
            "liaise",
        ]
    )
    informed = any(
        keyword in lower for keyword in ["status", "report", "updates", "provides", "communication", "issues"]
    )
    return responsible, accountable, consulted, informed


@dataclass
class CrossLink:
    sop_id: str
    title: Optional[str]
    span: TextSpan


def find_cross_links(lines: List[str]) -> List[CrossLink]:
    links: List[CrossLink] = []
    pattern = re.compile(r"SOP[\s-](\d{4})")
    for idx, line in enumerate(lines, start=1):
        for match in pattern.finditer(line):
            sop_id = match.group(1)
            remainder = line[match.end() :]
            title_match = re.search(r":\s*\*?([^*]+?)\*?\s*(?:$|,|;)", remainder)
            title = title_match.group(1).strip() if title_match else None
            links.append(CrossLink(sop_id=sop_id, title=title, span=TextSpan(line.strip(), idx, idx)))
    return links


def extract_scope_summary(section_lines: List[Tuple[int, str]]) -> Optional[TextSpan]:
    paragraphs: List[List[Tuple[int, str]]] = []
    current: List[Tuple[int, str]] = []
    for line_no, line in section_lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("---"):
            if current:
                paragraphs.append(current)
                current = []
            continue
        if stripped.startswith(("*", "-")):
            if current:
                paragraphs.append(current)
                current = []
            continue
        current.append((line_no, stripped))
    if current:
        paragraphs.append(current)
    if paragraphs:
        lines_flat = [text for _, text in paragraphs[0]]
        start = paragraphs[0][0][0]
        end = paragraphs[0][-1][0]
        return TextSpan(" ".join(lines_flat), start, end)
    return None


def citation(path: Path, span: TextSpan) -> str:
    relative = path.relative_to(ROOT)
    return f"【F:{relative.as_posix()}†L{span.start}-L{span.end}】"


def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    sop_files = sorted(
        [p for p in SOPS_DIR.glob("SOP-*.md") if re.search(r"SOP-(\d{4})", p.name)],
        key=lambda p: int(re.search(r"SOP-(\d{4})", p.name).group(1)),
    )
    for sop_path in sop_files:
        lines = read_lines(sop_path)
        indices = section_indices(lines)

        objective_lines = section_slice(lines, indices, ["Objective", "Purpose"])
        scope_lines = section_slice(lines, indices, ["Scope"])
        roles_lines = section_slice(lines, indices, ["Roles", "Responsibilities"])
        procedure_lines = section_slice(lines, indices, ["Procedure", "Activities"])

        objective_para = extract_paragraph(objective_lines)
        scope_para = extract_scope_summary(scope_lines)
        objective_items = collect_numbered_items(objective_lines)
        subheadings = collect_subheadings(procedure_lines)
        step_blocks = collect_step_blocks(procedure_lines)
        deliverables = collect_deliverables(procedure_lines)
        role_rows = collect_roles(roles_lines)
        cross_refs = find_cross_links(lines)

        if not objective_items and objective_para:
            objective_items = [objective_para]

        sop_id = re.search(r"SOP-(\d{4})", sop_path.name).group(1)
        raw_title = lines[0].strip().strip("# ")
        title = raw_title.replace("**", "").strip()

        output_lines: List[str] = []
        output_lines.append(f"# SOP-{sop_id} — {title}")
        output_lines.append("")

        if objective_para or scope_para:
            output_lines.append("## Preamble")
            if objective_para:
                output_lines.append(f"{objective_para.text} {citation(sop_path, objective_para)}")
            if scope_para:
                output_lines.append(f"{scope_para.text} {citation(sop_path, scope_para)}")
            output_lines.append("")

        if objective_items:
            output_lines.append("## Learning Objectives")
            for item in objective_items:
                output_lines.append(f"- {item.text} {citation(sop_path, item)}")
            output_lines.append("")

        if subheadings:
            output_lines.append("## Topics")
            for heading in subheadings:
                output_lines.append(f"- {heading.text} {citation(sop_path, heading)}")
            output_lines.append("")

        if step_blocks:
            output_lines.append("## Activities / Assignments")
            for idx, block in enumerate(step_blocks[:2], start=1):
                output_lines.append(f"{idx}) {block.text} {citation(sop_path, block)}")
            output_lines.append("")

        if deliverables:
            output_lines.append("## Deliverables & Artifacts")
            for span in deliverables:
                output_lines.append(f"- {span.text} {citation(sop_path, span)}")
            output_lines.append("")

        if role_rows:
            output_lines.append("## Roles / RACI (light)")
            output_lines.append("| Role | R | A | C | I |")
            output_lines.append("|---|---|---|---|---|")
            for role, resp_span in role_rows:
                r, a, c, i_flag = classify_raci(resp_span.text)
                role_text = f"{role} {citation(sop_path, resp_span)}"
                output_lines.append(
                    "| "
                    + " | ".join(
                        [
                            role_text,
                            "✓" if r else "",
                            "✓" if a else "",
                            "✓" if c else "",
                            "✓" if i_flag else "",
                        ]
                    )
                    + " |"
                )
            output_lines.append("")

        gates = []
        gate_pattern = re.compile(r"Gate\s*(\d+)")
        for span in step_blocks:
            match = gate_pattern.search(span.text)
            if match:
                gate_id = match.group(1)
                gates.append((f"G-{gate_id}", span))
        if gates:
            seen = set()
            output_lines.append("## Gates & Reviews")
            for gate_name, span in gates:
                if gate_name in seen:
                    continue
                seen.add(gate_name)
                output_lines.append(f"- **{gate_name}**: {span.text} {citation(sop_path, span)}")
            output_lines.append("")

        filtered_links = [link for link in cross_refs if link.sop_id != sop_id]
        if filtered_links:
            output_lines.append("## Cross-Links")
            seen_ids = set()
            for link in filtered_links:
                if link.sop_id in seen_ids:
                    continue
                seen_ids.add(link.sop_id)
                title_part = f" {link.title}" if link.title else ""
                output_lines.append(
                    f"- See: SOP-{link.sop_id}{title_part} {citation(sop_path, link.span)}"
                )
            output_lines.append("")

        output_path = OUTPUT_DIR / f"SOP-{sop_id}.md"
        output_path.write_text("\n".join(output_lines).strip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
