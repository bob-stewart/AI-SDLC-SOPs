from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from datetime import datetime

class PolarScore(BaseModel):
    """
    Polar Identity Score Factors.
    """
    competence: float = Field(0.0, ge=0.0, le=1.0)
    integrity: float = Field(0.0, ge=0.0, le=1.0)
    history: float = Field(0.0, ge=0.0, le=1.0)
    alignment: float = Field(0.0, ge=0.0, le=1.0)

    @property
    def magnitude(self) -> float:
        """Overall trust magnitude (average)."""
        return (self.competence + self.integrity + self.history + self.alignment) / 4

class IdentityProfile(BaseModel):
    id: str
    public_key: str
    alias: str
    polar_score: PolarScore = Field(default_factory=PolarScore)
    trustees: List[str] = [] # List of IDs who vouch for this entity
    is_verified: bool = False
    joined_at: datetime = Field(default_factory=datetime.now)

class OdentityEngine:
    """
    Odentity™ Engine.
    Manages Identity, Polar Scoring, and the PACE Plan (Web of Trust).
    """

    # PACE Plan: 4 Trustees required for verification
    PACE_THRESHOLD = 4 

    def __init__(self):
        self.identities: Dict[str, IdentityProfile] = {}

    def register_identity(self, alias: str, public_key: str) -> IdentityProfile:
        """
        Register a new unverified identity.
        """
        # In a real system, ID would be derived from public key
        new_id = f"did:aegis:{public_key[:8]}" 
        profile = IdentityProfile(
            id=new_id,
            public_key=public_key,
            alias=alias
        )
        self.identities[new_id] = profile
        return profile

    def endorse(self, endorser_id: str, target_id: str):
        """
        Endorse an identity (Vouch).
        Enforces PACE Plan logic.
        """
        endorser = self.identities.get(endorser_id)
        target = self.identities.get(target_id)

        if not endorser or not target:
            raise ValueError("Identity not found.")

        if not endorser.is_verified:
            raise ValueError("Endorser must be verified to vouch for others.")

        if endorser_id in target.trustees:
            return # Already endorsed

        target.trustees.append(endorser_id)
        self._recalculate_verification(target)

    def _recalculate_verification(self, profile: IdentityProfile):
        """
        Check if PACE Plan threshold is met.
        """
        if len(profile.trustees) >= self.PACE_THRESHOLD:
            profile.is_verified = True
            # Boost score based on trustees (Viral Coefficient)
            # Simplified logic: Average of trustees' scores
            total_mag = 0.0
            for t_id in profile.trustees:
                trustee = self.identities.get(t_id)
                if trustee:
                    total_mag += trustee.polar_score.magnitude
            
            avg_trust = total_mag / len(profile.trustees)
            # Initial bootstrap score
            profile.polar_score = PolarScore(
                competence=avg_trust * 0.8,
                integrity=avg_trust * 0.9,
                history=0.1,
                alignment=0.5
            )
