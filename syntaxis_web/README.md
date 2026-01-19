# 🌐 SYNTAXIS: The Interface Layer

**SYNTAXIS** is the visualization engine for the MeshCORE AI-SDLC. It serves as a "HyperCard for the mind," providing a dynamic, visual interface for humans and AI agents to observe, navigate, and edit the governance circuit.

## 🚀 Purpose

In a system governed by the **AEGIS** Digital Constitution, SYNTAXIS provides the human-readable layer. It translates the abstract Combinator Graph Reduction (CGR) logic and the complex **SOP Library** into interactive workflows and real-time governance status.

## 🛠️ Tech Stack

- **Framework**: React 18 + TypeScript
- **Build Tool**: Vite
- **State Management**: Integrated with the Aeonsynthesis MCP Holon.

## 🏗️ Getting Started

### Prerequisites
Ensure the **Aeonsynthesis Holon** is running in the root directory:
```bash
python aeonsynthesis_mcp/holon.py
```

### Installation
```bash
cd syntaxis_web
npm install
```

### Development
```bash
npm run dev
```

## 🔌 Connection to Governance

SYNTAXIS interfaces with the `/sops` and `/diagrams` directories to provide:
- **Interactive SOP Navigation**: Browse the 40 AI-SDLC SOPs with embedded visual workflows.
- **Audit Trails**: Visualize the **EXOCHAIN** immutable ledger.
- **Verification Monitoring**: Real-time status of safety invariants enforced by AEGIS.

---
*For the underlying logic, see [aegis_backend/](../aegis_backend/). For the manual, visit the [SOP Library](../sops/README.md).*
