import hashlib
import json
import sqlite3
import os
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
    Now backed by SQLite for persistence.
    """

    def __init__(self, db_path: str = "ledger.db"):
        self.db_path = db_path
        self.chain: List[Block] = []
        self._init_db()
        self._load_chain()

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS blocks (
                idx INTEGER PRIMARY KEY,
                timestamp TEXT,
                data TEXT,
                previous_hash TEXT,
                hash TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def _load_chain(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT idx, timestamp, data, previous_hash, hash FROM blocks ORDER BY idx ASC')
        rows = cursor.fetchall()
        conn.close()

        self.chain = []
        for row in rows:
            self.chain.append(Block(
                index=row[0],
                timestamp=row[1],
                data=json.loads(row[2]),
                previous_hash=row[3],
                hash=row[4]
            ))

    def create_block(self, data: dict, previous_hash: Optional[str] = None) -> Block:
        """
        Create a new block in the ledger and save to DB.
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
        
        self._save_block(block)
        self.chain.append(block)
        return block

    def _save_block(self, block: Block):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO blocks (idx, timestamp, data, previous_hash, hash) VALUES (?, ?, ?, ?, ?)',
            (block.index, block.timestamp, json.dumps(block.data), block.previous_hash, block.hash)
        )
        conn.commit()
        conn.close()

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
