# 🛡️ AEGIS: The Digital Constitution

**AEGIS** is the core logic engine of the MeshCORE governance framework. It operates as a "Digital Constitution," enforcing safety invariants and ethical rules directly within the computation layer.

## ⚙️ Core Mechanism

AEGIS uses **Combinator Graph Reduction (CGR)** to verify that every action proposed by an AI agent or a human user complies with the system's foundational invariants. 

- **Invariant Enforcement**: Actions that violate the CGR type system or the **AI-IRB** rules are rejected at the logic level.
- **Exochain Integration**: Every verified state change is recorded on the **EXOCHAIN**, an immutable ledger for audit and transparency.

## 📂 Project Structure

- **[/core](core/)**: The primary logic for state management and invariant verification.
- **[/vm](vm/)**: The virtual machine executing the CGR reduction.
- **[/crypto](crypto/)**: Cryptographic functions for anchoring state to the Exochain.
- **[/exochain](exochain/)**: The storage and consensus logic for the immutable memory.
- **`genesis_protocol.yaml`**: The initial configuration of the Digital Constitution.

## 🚀 Execution

The backend is exposed via the **Aeonsynthesis MCP Holon**. To run the core logic in a development environment:

```bash
python aegis_backend/main.py
```

## 🔒 Governance Integration

AEGIS acts as the automated enforcer for the **[AI-SDLC SOPs](../sops/README.md)**. While the SOPs provide the human-readable narrative and IRB process, AEGIS provides the technical "teeth" to ensure those procedures are not bypassed.

---
*For the visual interface, see [syntaxis_web/](../syntaxis_web/). for the manual, visit the [SOP Library](../sops/README.md).*
