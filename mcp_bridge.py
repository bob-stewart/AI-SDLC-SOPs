import sys
import json
import requests

# The Dockerized Holon Endpoint
HOLON_URL = "http://localhost:9000/mcp"

def main():
    """
    Bridges Stdio (IDE) to HTTP (Holon Container).
    """
    for line in sys.stdin:
        try:
            request = json.loads(line)
            
            # Forward to Holon
            response = requests.post(HOLON_URL, json=request)
            response.raise_for_status()
            
            # Write response back to Stdio
            sys.stdout.write(json.dumps(response.json()) + "\n")
            sys.stdout.flush()
            
        except Exception as e:
            # Log error to stderr so it doesn't break the JSON-RPC pipe
            sys.stderr.write(f"Bridge Error: {e}\n")
            sys.stderr.flush()

if __name__ == "__main__":
    main()
