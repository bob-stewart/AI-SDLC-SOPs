from typing import Dict, Any
from .types import GovernanceGraph, ReductionResult

class Sentinel:
    """
    The Sentinel Hypervisor.
    Enforces the 'Constitution' (Invariants) on the VM.
    """

    def __init__(self):
        pass

    def enforce_invariants(self, vm_state: Dict[str, Any]):
        """
        Check system-level invariants.
        """
        if not vm_state.get("active_protocol_hash"):
            raise RuntimeError("SENTINEL ALERT: VM running without Active Protocol!")
        
        print("Sentinel: System Invariants Verified.")

    def check_pre_execution(self, graph: GovernanceGraph):
        """
        Check inputs before execution.
        """
        # Example: Prevent empty graphs
        if not graph.nodes:
            raise ValueError("SENTINEL ALERT: Attempted to execute empty graph.")
        
        print("Sentinel: Pre-Execution Checks Passed.")

    def check_post_execution(self, result: ReductionResult):
        """
        Check outputs after execution.
        """
        # Example: Ensure decision is valid
        if result.decision not in ["APPROVED", "REJECTED", "DEFERRED"]:
            raise ValueError(f"SENTINEL ALERT: Invalid decision value: {result.decision}")
        
        print("Sentinel: Post-Execution Checks Passed.")
