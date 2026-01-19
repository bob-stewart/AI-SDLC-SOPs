import requests
import json
import time

BASE_URL = "http://localhost:8000"

def print_step(step):
    print(f"\n=== {step} ===")

def verify():
    # Wait for server to start (manual step usually, but we assume it's running or we run it)
    print("Checking Health...")
    try:
        r = requests.get(f"{BASE_URL}/")
        print(r.json())
    except:
        print("Server not running. Please start 'python aegis_backend/main.py'")
        return

    # 1. Genesis Ceremony
    print_step("1. Genesis Ceremony")
    trustees = ["key_alice", "key_bob", "key_charlie", "key_dave", "key_eve"]
    payload = {
        "trustees": trustees,
        "threshold": 3
    }
    r = requests.post(f"{BASE_URL}/genesis", json=payload)
    if r.status_code == 200:
        print("SUCCESS:", json.dumps(r.json(), indent=2))
    else:
        print("FAILED:", r.text)
        return

    # 2. Register Identity
    print_step("2. Register Identity")
    payload = {
        "alias": "Dr. S. Hawking",
        "public_key": "key_hawking_001"
    }
    r = requests.post(f"{BASE_URL}/identity/register", json=payload)
    print(r.json())

    # 3. Submit Proposal
    print_step("3. Submit Proposal")
    # Construct a simple graph
    graph = {
        "nodes": [
            {
                "id": "prop-1",
                "type": "PROPOSAL",
                "title": "Deploy Model M2",
                "content": "Deploying the new reasoning model.",
                "author_id": "did:aegis:key_hawk",
                "effects": {"risk": 0.1, "fairness": 0.9, "privacy": 0.5, "novelty": 0.8, "security": 0.9}
            },
            {
                "id": "ev-1",
                "type": "EVIDENCE",
                "title": "Fairness Report",
                "content": "Bias metrics are within range.",
                "author_id": "did:aegis:key_hawk",
                "effects": {"risk": 0.0, "fairness": 0.9, "privacy": 0.0, "novelty": 0.0, "security": 0.0}
            }
        ],
        "edges": [
            {
                "source": "prop-1",
                "target": "ev-1",
                "relation": "SUPPORTS",
                "weight": 1.0
            }
        ]
    }
    r = requests.post(f"{BASE_URL}/proposal", json=graph)
    print(json.dumps(r.json(), indent=2))

    # 4. Check Ledger
    print_step("4. Check Ledger")
    r = requests.get(f"{BASE_URL}/ledger")
    print(json.dumps(r.json(), indent=2))

if __name__ == "__main__":
    verify()
