from typing import Dict, Any
from core.types import GovernanceGraph, ReductionResult
from core.cgr import CGREngine
from core.sentinel import Sentinel # We will implement this next

class AegisVM:
    """
    The Governance Virtual Machine.
    Orchestrates the execution of Governance Protocols.
    """

    def __init__(self):
        self.cgr = CGREngine()
        self.sentinel = Sentinel()
        self.state: Dict[str, Any] = {
            "boot_time": None,
            "active_protocol_hash": None,
            "cycle_count": 0
        }

    def boot(self, genesis_block_hash: str):
        """
        Boot the VM from the Genesis Block.
        """
        # 1. Verify Genesis Block (Mock for now, will connect to ExoChain)
        print(f"Booting AEGIS VM from Root: {genesis_block_hash}")
        self.state["active_protocol_hash"] = genesis_block_hash
        self.state["boot_time"] = "NOW"
        
        # 2. Check Invariants
        self.sentinel.enforce_invariants(self.state)

    def execute(self, graph: GovernanceGraph) -> ReductionResult:
        """
        Execute a Governance Graph (Proposal).
        """
        self.state["cycle_count"] += 1
        
        # 1. Pre-Execution Sentinel Check
        self.sentinel.check_pre_execution(graph)

        # 2. Run CGR
        result = self.cgr.reduce(graph)

        # 3. Post-Execution Sentinel Check
        self.sentinel.check_post_execution(result)

        return result

    def hot_swap(self, new_protocol_hash: str):
        """
        Self-Modification: Load a new protocol.
        """
        print(f"Hot-swapping Protocol to: {new_protocol_hash}")
        # In a real implementation, we would fetch the code from ExoChain here
        self.state["active_protocol_hash"] = new_protocol_hash
        self.sentinel.enforce_invariants(self.state)
