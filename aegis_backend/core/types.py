from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Union, Literal, Any
from enum import Enum
from datetime import datetime

# --- Effect Algebra ---

class EffectType(str, Enum):
    RISK = "RISK"
    FAIRNESS = "FAIRNESS"
    PRIVACY = "PRIVACY"
    NOVELTY = "NOVELTY"
    SECURITY = "SECURITY"

class EffectVector(BaseModel):
    risk: float = Field(0.0, ge=0.0, le=1.0)
    fairness: float = Field(0.0, ge=0.0, le=1.0)
    privacy: float = Field(0.0, ge=0.0, le=1.0)
    novelty: float = Field(0.0, ge=0.0, le=1.0)
    security: float = Field(0.0, ge=0.0, le=1.0)

# --- Governance IR Nodes ---

class NodeType(str, Enum):
    PROPOSAL = "PROPOSAL"
    CLAIM = "CLAIM"
    EVIDENCE = "EVIDENCE"
    POLICY = "POLICY"
    VOTE = "VOTE"
    DECISION = "DECISION"
    AMENDMENT = "AMENDMENT" # Self-modification

class GovernanceNode(BaseModel):
    id: str
    type: NodeType
    title: str
    content: str
    author_id: str
    timestamp: datetime = Field(default_factory=datetime.now)
    effects: EffectVector = Field(default_factory=EffectVector)
    metadata: Dict[str, Any] = Field(default_factory=dict)

class GovernanceEdge(BaseModel):
    source: str
    target: str
    relation: str # e.g., "SUPPORTS", "REFUTES", "REQUIRES"
    weight: float = 1.0

class GovernanceGraph(BaseModel):
    nodes: List[GovernanceNode]
    edges: List[GovernanceEdge]

# --- CGR Types ---

class ReductionResult(BaseModel):
    decision: Literal["APPROVED", "REJECTED", "DEFERRED"]
    trace: List[str] # Explanation of the reduction
    final_effects: EffectVector
