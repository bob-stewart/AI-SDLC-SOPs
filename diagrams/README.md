# 🖼️ Diagram Catalog

This directory houses the visual counterparts to the **AI-SDLC Standard Operating Procedures**. Each diagram illustrates the flow of responsibilities, decision checkpoints, and AI-IRB gates described in the narrative SOP documents.

## 📂 Asset Types

For every SOP, we maintain three formats to support different governance needs:

- **PlantUML Sources (`.puml`)**: The source-of-truth text definitions. These allow for version-controlled changes to process logic.
- **SVG Exports (`.svg`)**: Scalable vector graphics for browser-based viewing and high-quality documentation.
- **PNG Exports (`.PNG`)**: High-resolution raster images used for embedding directly into the [Markdown SOPs](../sops/README.md).

## 🔗 Synchronization

File names follow the SOP identifier pattern (`SOP-####-##-AI`) to ensure a 1:1 mapping with the [SOP Library](../sops/).

| SOP ID | Narrative Procedure | Visual Workflow |
| :--- | :--- | :--- |
| **SOP-1000** | [SOP-1000-01-AI](../sops/SOP-1000-01-AI_AI-Integrated-Program-and-Project-Management.md) | [View PNG](SOP-1000-01-AI.PNG) |
| **SOP-1006** | [SOP-1006-01-AI](../sops/SOP-1006-01-AI_AI-IRB-Engagement-and-Ethical-Review-Procedure.md) | [View PNG](SOP-1006-01-AI.PNG) |
| ... | *Refer to the [Full Index](../sops/SOP-LIST-01-AI_AI-IRB-Governed-AI-SDLC.md) for a complete list.* | |

## 🛠️ Maintenance

When a governance process changes:
1.  **Modify** the `.puml` file in this directory.
2.  **Regenerate** the `.svg` and `.PNG` assets.
3.  **Verify** the changes against the narrative text in the corresponding `../sops/` file.

---
*For the detailed procedural narratives, visit the [SOP Library](../sops/README.md).*
