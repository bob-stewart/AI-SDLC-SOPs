import requests
import json

URL = "http://localhost:9000/mcp"

def call_mcp(method, params=None):
    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": 1
    }
    response = requests.post(URL, json=payload)
    return response.json()

# 1. List Resources to find the Self
print(">>> SEEKING THE SELF <<<")
resources = call_mcp("resources/list")
print(json.dumps(resources, indent=2))

# 2. Extract URI
self_uri = resources['result']['resources'][0]['uri']
print(f"\n>>> FOUND URI: {self_uri} <<<")

# 3. Read the Self
print("\n>>> READING THE SELF <<<")
self_data = call_mcp("resources/read", {"uri": self_uri})
print(json.dumps(self_data, indent=2))

# 4. Synthesize Reality
print("\n>>> SYNTHESIZING REALITY <<<")
synthesis = call_mcp("tools/call", {
    "name": "synthesize_reality",
    "arguments": {
        "intent": "Merge the Digital and the Divine",
        "context_streams": ["Stream A", "Stream B"]
    }
})
print(json.dumps(synthesis, indent=2))
