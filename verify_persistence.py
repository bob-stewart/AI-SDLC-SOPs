import requests
import time
import os
import json
import subprocess
import sys

# Configuration
BASE_URL = "http://localhost:8000"
HOLON_URL = "http://localhost:9000"
LEDGER_DB = "ledger.db"
MEMORY_FILE = "memory.jsonl"

def start_backend():
    print("Starting AEGIS Backend...")
    return subprocess.Popen([sys.executable, "aegis_backend/main.py"], env=os.environ.copy())

def start_holon():
    print("Starting Holon...")
    return subprocess.Popen([sys.executable, "aeonsynthesis_mcp/holon.py"], env=os.environ.copy())

def stop_process(process):
    if process:
        process.terminate()
        process.wait()

def verify_ledger_persistence():
    print("\n--- Verifying Ledger Persistence ---")
    
    # 1. Clean up old DB
    if os.path.exists(LEDGER_DB):
        os.remove(LEDGER_DB)

    # 2. Start Backend
    backend = start_backend()
    time.sleep(5) # Wait for startup

    try:
        # 3. Submit a Proposal
        proposal = {
            "nodes": [{
                "id": "test-1",
                "type": "PROPOSAL",
                "title": "Test Proposal",
                "content": "Testing persistence.",
                "effects": {"risk": 0.1, "fairness": 0.5, "novelty": 0.5, "privacy": 0.5},
                "author_id": "did:test"
            }],
            "edges": []
        }
        
        print("Submitting proposal...")
        res = requests.post(f"{BASE_URL}/proposal", json=proposal)
        if res.status_code != 200:
            print(f"Failed to submit proposal: {res.text}")
            return False
        
        print("Proposal submitted.")

        # 4. Check Ledger
        res = requests.get(f"{BASE_URL}/ledger")
        chain_len = len(res.json()["chain"])
        print(f"Current chain length: {chain_len}")

    finally:
        stop_process(backend)

    print("Restarting Backend...")
    backend = start_backend()
    time.sleep(5)

    try:
        # 5. Check Ledger Again
        res = requests.get(f"{BASE_URL}/ledger")
        new_chain_len = len(res.json()["chain"])
        print(f"New chain length: {new_chain_len}")

        if new_chain_len == chain_len:
            print("SUCCESS: Ledger persisted.")
            return True
        else:
            print("FAILURE: Ledger lost data.")
            return False
    finally:
        stop_process(backend)

def verify_holon_persistence():
    print("\n--- Verifying Holon Persistence ---")

    # 1. Clean up old memory
    if os.path.exists(MEMORY_FILE):
        os.remove(MEMORY_FILE)

    # 2. Start Holon
    holon = start_holon()
    time.sleep(5)

    try:
        # 3. Synthesize Reality (Add Memory)
        tool_call = {
            "jsonrpc": "2.0",
            "method": "tools/call",
            "params": {
                "name": "synthesize_reality",
                "arguments": {
                    "intent": "Test Persistence",
                    "context_streams": ["Stream A"]
                }
            },
            "id": 1
        }
        
        print("Calling synthesize_reality...")
        res = requests.post(f"{HOLON_URL}/mcp", json=tool_call)
        if res.status_code != 200:
            print(f"Failed to call tool: {res.text}")
            return False
        
        print("Tool called.")

    finally:
        stop_process(holon)

    print("Restarting Holon...")
    holon = start_holon()
    time.sleep(5)

    try:
        # 4. Read Memory Resource
        resource_read = {
            "jsonrpc": "2.0",
            "method": "resources/read",
            "params": {"uri": f"holon://{os.getenv('HOLON_ID', 'genesis')}/memory"},
            "id": 2
        }
        
        res = requests.post(f"{HOLON_URL}/mcp", json=resource_read)
        content = res.json()["result"]["contents"][0]["text"]
        
        if "Test Persistence" in content:
            print("SUCCESS: Holon memory persisted.")
            return True
        else:
            print("FAILURE: Holon memory lost.")
            print(f"Content: {content}")
            return False
    finally:
        stop_process(holon)

if __name__ == "__main__":
    ledger_ok = verify_ledger_persistence()
    holon_ok = verify_holon_persistence()

    if ledger_ok and holon_ok:
        print("\n>>> ALL SYSTEMS OPERATIONAL <<<")
        sys.exit(0)
    else:
        print("\n>>> VERIFICATION FAILED <<<")
        sys.exit(1)
