# System Walkthrough

## Current Status
**System Version**: 0.1.0 (Alpha)
**Verification Status**: PASSING

## Components

### 1. AEGIS Backend (The Logic)
*   **Location**: `aegis_backend/`
*   **State**: Implemented
*   **Key Features**:
    *   `core/`: Basic Combinator Graph Reduction engine.
    *   `crypto/`: Quantum-resistant hashing (placeholder).
    *   `exochain/`: Local ledger implementation.

### 2. Syntaxis Web (The Interface)
*   **Location**: `syntaxis_web/`
*   **State**: Prototype
*   **Key Features**:
    *   Visualizer for the CGR graph.
    *   Dashboard for system metrics.

### 3. Aeonsynthesis MCP (The Network)
*   **Location**: `aeonsynthesis_mcp/`
*   **State**: Active
*   **Key Features**:
    *   `holon.py`: The main MCP server entry point.
    *   `mcp_bridge.py`: Bridge between local context and the Holon.

## Verification Results

### Unit Tests
```bash
$ cargo test
running 12 tests
test result: ok. 12 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out
```

### Integration Tests
```bash
$ python verify_backend.py
[INFO] Connecting to Holon...
[INFO] Verifying Invariants...
[SUCCESS] All systems nominal.
```

## How to Run
1.  **Start the Backend**:
    ```bash
    cd aegis_backend
    docker-compose up -d
    ```
2.  **Start the MCP Server**:
    ```bash
    python aeonsynthesis_mcp/holon.py
    ```
3.  **Launch the UI**:
    ```bash
    cd syntaxis_web
    npm run dev
    ```
