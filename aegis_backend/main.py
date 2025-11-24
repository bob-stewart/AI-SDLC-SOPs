from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import uvicorn

# Import Core Components
from core.types import GovernanceGraph, ReductionResult
from core.cgr import CGREngine
from vm.engine import AegisVM
from exochain.ledger import MerkleLedger
from exochain.identity import OdentityEngine
from core.genesis import GenesisCeremony

app = FastAPI(
    title="AEGIS Backend",
    description="The Logic & Trust Engine for the Trinity Architecture.",
    version="0.1.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- System State (In-Memory for MVP) ---
ledger = MerkleLedger()
vm = AegisVM()
identity_engine = OdentityEngine()
genesis_ceremony = GenesisCeremony(ledger, vm)

# --- API Models ---

class GenesisRequest(BaseModel):
    trustees: List[str]
    threshold: int

class IdentityRequest(BaseModel):
    alias: str
    public_key: str

# --- Endpoints ---

@app.get("/")
async def root():
    return {
        "status": "AEGIS ENGINE ONLINE",
        "version": "0.1.0",
        "vm_state": vm.state,
        "ledger_height": len(ledger.chain)
    }

@app.post("/genesis")
async def trigger_genesis(request: GenesisRequest):
    """
    Trigger the Genesis Ceremony.
    """
    try:
        result = genesis_ceremony.perform_ceremony(request.trustees, request.threshold)
        return {"status": "GENESIS_COMPLETE", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/identity/register")
async def register_identity(request: IdentityRequest):
    """
    Register a new Identity.
    """
    try:
        profile = identity_engine.register_identity(request.alias, request.public_key)
        return {"status": "REGISTERED", "profile": profile}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/proposal")
async def submit_proposal(graph: GovernanceGraph):
    """
    Submit a Governance Graph for Execution (Reduction).
    """
    try:
        # 1. Execute in VM
        result = vm.execute(graph)
        
        # 2. Anchor Decision to Ledger
        ledger.create_block({
            "event": "DECISION",
            "proposal_id": graph.nodes[0].id if graph.nodes else "UNKNOWN",
            "result": result.dict()
        })
        
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/ledger")
async def get_ledger():
    """
    View the Immutable Ledger.
    """
    return {"chain": ledger.chain}

import os

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
