import yaml
import json
from typing import List, Dict, Any
from crypto.shamir import ShamirSecretSharing, generate_root_key
from exochain.ledger import MerkleLedger
from vm.engine import AegisVM

class GenesisCeremony:
    """
    The Bootstrap Ceremony.
    1. Generates Root Key.
    2. Splits Key (Shamir).
    3. Anchors Genesis Protocol to Ledger.
    4. Boots VM.
    """

    def __init__(self, ledger: MerkleLedger, vm: AegisVM):
        self.ledger = ledger
        self.vm = vm

    def perform_ceremony(self, trustees: List[str], threshold: int) -> Dict[str, Any]:
        """
        Execute the ceremony.
        trustees: List of Trustee IDs (Public Keys).
        threshold: Number of shares required to recover (K).
        """
        print("--- INITIATING GENESIS CEREMONY ---")

        # 1. Generate Root Key
        root_key = generate_root_key()
        print(f"1. Root Key Generated (Bit length: {root_key.bit_length()})")

        # 2. Split Key (PACE Plan / Shamir)
        # We generate len(trustees) shares
        shares = ShamirSecretSharing.split(root_key, len(trustees), threshold)
        print(f"2. Root Key Split into {len(shares)} shares (Threshold: {threshold})")

        # Map shares to trustees (In real life, secure distribution happens here)
        trustee_shares = {t_id: share for t_id, share in zip(trustees, shares)}

        # 3. Load Genesis Protocol
        with open("aegis_backend/genesis_protocol.yaml", "r") as f:
            protocol_data = yaml.safe_load(f)
        
        print("3. Genesis Protocol Loaded.")

        # 4. Anchor to Ledger (Genesis Block)
        genesis_data = {
            "event": "GENESIS_BOOTSTRAP",
            "protocol": protocol_data,
            "trustee_ids": trustees,
            "threshold": threshold,
            # We do NOT store the root key or shares on the ledger!
            "root_key_verification": "SHA256_HASH_OF_ROOT_KEY_HERE" # Placeholder for Zero-Knowledge Proof
        }
        
        genesis_block = self.ledger.create_block(genesis_data, previous_hash="0"*64)
        print(f"4. Genesis Block Anchored: {genesis_block.hash}")

        # 5. Boot VM
        self.vm.boot(genesis_block.hash)
        print("5. AEGIS VM Booted.")

        return {
            "genesis_hash": genesis_block.hash,
            "trustee_shares": trustee_shares # Return shares to be distributed to users
        }
