import hashlib
import json
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

class Block(BaseModel):
    index: int
    timestamp: str
    data: dict
    previous_hash: str
    hash: str

class MerkleLedger:
    """
    Cryptographically secured append-only ledger (Simplified Blockchain).
    Uses SHA-256 for hashing.
    """

    def __init__(self):
        self.chain: List[Block] = []
        # Create generic genesis block (placeholder, real one comes from Ceremony)
        # self.create_block(data={"event": "LEDGER_INIT"}, previous_hash="0") 

    def create_block(self, data: dict, previous_hash: Optional[str] = None) -> Block:
        """
        Create a new block in the ledger.
        """
        if not previous_hash:
            previous_hash = self.chain[-1].hash if self.chain else "0"

        index = len(self.chain)
        timestamp = datetime.now().isoformat()
        
        block_content = {
            "index": index,
            "timestamp": timestamp,
            "data": data,
            "previous_hash": previous_hash
        }
        
        block_hash = self._hash_block(block_content)
        
        block = Block(
            index=index,
            timestamp=timestamp,
            data=data,
            previous_hash=previous_hash,
            hash=block_hash
        )
        
        self.chain.append(block)
        return block

    def get_last_block(self) -> Optional[Block]:
        return self.chain[-1] if self.chain else None

    @staticmethod
    def _hash_block(block_content: dict) -> str:
        """
        SHA-256 Hashing of block content.
        """
        block_string = json.dumps(block_content, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def verify_chain(self) -> bool:
        """
        Verify the integrity of the chain.
        """
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]

            if current.previous_hash != previous.hash:
                return False
            
            # Re-hash to check for tampering
            content = {
                "index": current.index,
                "timestamp": current.timestamp,
                "data": current.data,
                "previous_hash": current.previous_hash
            }
            if self._hash_block(content) != current.hash:
                return False
                
        return True
