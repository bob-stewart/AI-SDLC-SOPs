from typing import List, Dict, Any, Optional
from .types import GovernanceNode, GovernanceEdge, GovernanceGraph, NodeType, EffectVector, ReductionResult

class CGREngine:
    """
    Combinator Graph Reduction Engine.
    Reduces a Governance Graph to a single Decision.
    Now aligned with the Iron Core (Rust) rules.
    """

    def __init__(self):
        pass

    def reduce(self, graph: GovernanceGraph) -> ReductionResult:
        """
        Main entry point for reduction.
        """
        violations = []

        # Rule 1: Empty Graph
        if not graph.nodes:
            return ReductionResult(
                decision="REJECTED",
                reason="Graph is empty.",
                trace=["Violation: Graph must contain at least one node."],
                final_effects=EffectVector()
            )

        # Rule 2: Cycle Detection
        if self._has_cycle(graph):
            violations.append("Cycle detected in governance graph. Logic must be acyclic.")

        # Rule 3: Signature Verification (Stub)
        for node in graph.nodes:
            if not self._verify_signature(node):
                violations.append(f"Invalid signature for node '{node.title}'.")

        # Rule 4: Risk Threshold
        # Find the PROPOSAL node
        proposal = next((n for n in graph.nodes if n.type in [NodeType.PROPOSAL, NodeType.AMENDMENT]), graph.nodes[0])
        
        if proposal.effects.risk > 0.8:
            violations.append(f"Risk level {proposal.effects.risk:.2f} exceeds constitutional threshold of 0.8")

        # Rule 5: Fairness Floor
        if proposal.effects.fairness < 0.3:
            violations.append(f"Fairness level {proposal.effects.fairness:.2f} is below constitutional floor of 0.3")

        if violations:
            return ReductionResult(
                decision="REJECTED",
                reason="Constitutional invariants violated.",
                trace=violations,
                final_effects=proposal.effects
            )

        # If all checks pass, we can proceed with the recursive reduction (optional for MVP if we just want validation)
        # For now, we'll return APPROVED if invariants are met, matching the Rust MVP logic.
        
        return ReductionResult(
            decision="APPROVED",
            reason="Proposal satisfies all constitutional invariants.",
            trace=["All checks passed."],
            final_effects=proposal.effects
        )

    def _has_cycle(self, graph: GovernanceGraph) -> bool:
        adj = {node.id: [] for node in graph.nodes}
        for edge in graph.edges:
            if edge.source in adj:
                adj[edge.source].append(edge.target)
        
        visited = set()
        stack = set()

        def visit(node_id):
            if node_id in stack:
                return True
            if node_id in visited:
                return False
            
            visited.add(node_id)
            stack.add(node_id)

            for neighbor in adj.get(node_id, []):
                if visit(neighbor):
                    return True
            
            stack.remove(node_id)
            return False

        for node in graph.nodes:
            if visit(node.id):
                return True
        return False

    def _verify_signature(self, node: GovernanceNode) -> bool:
        # Stub: Check if author_id is present for PROPOSAL
        if node.type == NodeType.PROPOSAL and not node.author_id:
            return False
        return True
