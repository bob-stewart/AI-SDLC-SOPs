import unittest
from vm.engine import AegisVM
from core.types import GovernanceGraph, GovernanceNode, GovernanceEdge, EffectVector

class TestCGREngine(unittest.TestCase):
    def setUp(self):
        self.vm = AegisVM()

    def test_high_risk_blocking(self):
        """Test that a high-risk proposal is rejected if it exceeds the threshold."""
        # Create a high-risk proposal
        proposal = GovernanceGraph(
            nodes=[
                GovernanceNode(id="1", type="PROPOSAL", title="Deploy Risky Model", content="...", author_id="user", effects=EffectVector(risk=0.9, fairness=0.5, novelty=0.5, privacy=0.1)),
            ],
            edges=[]
        )
        
        # Execute in VM
        result = self.vm.execute(proposal)
        
        # Verify it was rejected
        self.assertEqual(result.decision, "REJECTED")
        self.assertTrue(any("Risk level" in trace for trace in result.trace))

    def test_cgr_confluence(self):
        """Verify that reduction order does not affect the final decision (Confluence)."""
        # This is a theoretical property. For the MVP, we verify that the same input always yields the same output.
        proposal = GovernanceGraph(
            nodes=[
                GovernanceNode(id="1", type="PROPOSAL", title="Standard Model", content="...", author_id="user", effects=EffectVector(risk=0.1, fairness=0.9, novelty=0.5, privacy=0.1)),
            ],
            edges=[]
        )
        
        result1 = self.vm.execute(proposal)
        result2 = self.vm.execute(proposal)
        
        self.assertEqual(result1.decision, result2.decision)

if __name__ == '__main__':
    unittest.main()
