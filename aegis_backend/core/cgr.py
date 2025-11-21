from typing import List, Dict, Any, Optional
from .types import GovernanceNode, GovernanceEdge, GovernanceGraph, NodeType, EffectVector, ReductionResult

class CGREngine:
    """
    Combinator Graph Reduction Engine.
    Reduces a Governance Graph to a single Decision.
    """

    def __init__(self):
        pass

    def reduce(self, graph: GovernanceGraph) -> ReductionResult:
        """
        Main entry point for reduction.
        """
        # 1. Find the "Root" node (usually the Proposal)
        root = self._find_root(graph)
        if not root:
            return ReductionResult(
                decision="REJECTED",
                trace=["Error: No Proposal Node found."],
                final_effects=EffectVector()
            )

        # 2. Recursively reduce the graph starting from the root
        trace = []
        decision, effects = self._reduce_node(root, graph, trace)

        return ReductionResult(
            decision=decision,
            trace=trace,
            final_effects=effects
        )

    def _find_root(self, graph: GovernanceGraph) -> Optional[GovernanceNode]:
        # Simple heuristic: The node with type PROPOSAL or AMENDMENT
        for node in graph.nodes:
            if node.type in [NodeType.PROPOSAL, NodeType.AMENDMENT]:
                return node
        return None

    def _reduce_node(self, node: GovernanceNode, graph: GovernanceGraph, trace: List[str]) -> (str, EffectVector):
        trace.append(f"Visiting Node: {node.title} ({node.type})")
        
        # Base Case: Evidence or Vote (Leaf nodes)
        if node.type == NodeType.EVIDENCE:
            trace.append(f"-> Evidence found: {node.effects}")
            return "APPROVED", node.effects # Evidence "exists", so it's approved context
        
        if node.type == NodeType.VOTE:
            # In a real system, we'd check the signature and vote value
            trace.append(f"-> Vote found: {node.content}")
            return "APPROVED", node.effects

        # Recursive Step: Reduce children (dependencies)
        children = self._get_children(node, graph)
        child_results = []
        
        accumulated_effects = node.effects.copy()

        for child in children:
            c_decision, c_effects = self._reduce_node(child, graph, trace)
            child_results.append(c_decision)
            # Accumulate effects (simplified vector addition)
            accumulated_effects.risk += c_effects.risk
            accumulated_effects.fairness += c_effects.fairness
            # ... others

        # Combinator Logic (The "Physics")
        decision = "APPROVED"
        
        # 1. Veto Logic
        if "REJECTED" in child_results:
            decision = "REJECTED"
            trace.append("-> Vetoed by dependency.")

        # 2. Policy Logic (if this node is a Policy)
        if node.type == NodeType.POLICY:
            # Example: Risk Threshold
            if accumulated_effects.risk > 0.5: # Mock threshold
                decision = "REJECTED"
                trace.append(f"-> Policy Violation: Risk {accumulated_effects.risk} > 0.5")
            else:
                trace.append("-> Policy Passed.")

        trace.append(f"Result for {node.title}: {decision}")
        return decision, accumulated_effects

    def _get_children(self, node: GovernanceNode, graph: GovernanceGraph) -> List[GovernanceNode]:
        children = []
        for edge in graph.edges:
            if edge.source == node.id:
                target = next((n for n in graph.nodes if n.id == edge.target), None)
                if target:
                    children.append(target)
        return children
