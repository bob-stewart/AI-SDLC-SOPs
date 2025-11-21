import unittest
import requests
import time

BASE_URL = "http://localhost:8000"

class TestAegisAPI(unittest.TestCase):
    def test_status_endpoint(self):
        """Verify the / endpoint returns online status."""
        try:
            response = requests.get(f"{BASE_URL}/")
            self.assertEqual(response.status_code, 200)
            data = response.json()
            self.assertEqual(data['status'], "AEGIS ENGINE ONLINE")
            self.assertIsInstance(data['ledger_height'], int)
        except requests.exceptions.ConnectionError:
            self.fail("API is not reachable. Is the server running?")

    def test_proposal_submission(self):
        """Verify that a valid proposal can be submitted and returns a decision."""
        proposal = {
            "nodes": [
                {
                    "id": "1",
                    "type": "PROPOSAL",
                    "title": "Test Proposal",
                    "content": "Testing the API",
                    "author_id": "did:aegis:test",
                    "effects": {"risk": 0.1, "fairness": 0.5, "novelty": 0.5, "privacy": 0.1}
                }
            ],
            "edges": []
        }
        
        try:
            response = requests.post(f"{BASE_URL}/proposal", json=proposal)
            self.assertEqual(response.status_code, 200)
            data = response.json()
            self.assertIn(data['decision'], ["APPROVED", "REJECTED", "DEFERRED"])
        except requests.exceptions.ConnectionError:
            self.fail("API is not reachable. Is the server running?")

if __name__ == '__main__':
    unittest.main()
