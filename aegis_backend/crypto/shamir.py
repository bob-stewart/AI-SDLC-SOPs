import secrets
from typing import List, Tuple

class ShamirSecretSharing:
    """
    Implementation of Shamir's Secret Sharing.
    Splits a secret into N shares, requiring K to reconstruct.
    Uses a large prime field for security.
    """

    # A large prime number (Mersenne prime 2^127 - 1)
    PRIME = 2**127 - 1

    @staticmethod
    def _eval_poly(poly: List[int], x: int, prime: int) -> int:
        """Evaluates polynomial at x."""
        result = 0
        for coeff in reversed(poly):
            result = (result * x + coeff) % prime
        return result

    @staticmethod
    def _lagrange_interpolation(x: int, x_s: List[int], y_s: List[int], prime: int) -> int:
        """
        Reconstructs the secret (f(0)) using Lagrange interpolation.
        """
        k = len(x_s)
        secret = 0
        for j in range(k):
            numerator = 1
            denominator = 1
            for m in range(k):
                if m == j:
                    continue
                # L_j(0) = product( -x_m / (x_j - x_m) )
                numerator = (numerator * (-x_s[m])) % prime
                denominator = (denominator * (x_s[j] - x_s[m])) % prime
            
            # Modular inverse of denominator
            lagrange_coeff = (numerator * pow(denominator, -1, prime)) % prime
            secret = (secret + y_s[j] * lagrange_coeff) % prime
        
        return secret

    @classmethod
    def split(cls, secret: int, n: int, k: int) -> List[Tuple[int, int]]:
        """
        Split a secret integer into n shares, with threshold k.
        Returns a list of (x, y) tuples.
        """
        if k > n:
            raise ValueError("Threshold k cannot be greater than total shares n")
        
        # 1. Generate random polynomial coefficients [a_1, ..., a_{k-1}]
        # a_0 is the secret
        coeffs = [secret] + [secrets.randbelow(cls.PRIME) for _ in range(k - 1)]
        
        # 2. Generate shares (x, f(x)) for x = 1 to n
        shares = []
        for i in range(1, n + 1):
            x = i
            y = cls._eval_poly(coeffs, x, cls.PRIME)
            shares.append((x, y))
            
        return shares

    @classmethod
    def recover(cls, shares: List[Tuple[int, int]]) -> int:
        """
        Recover the secret from a list of (x, y) shares.
        """
        x_s, y_s = zip(*shares)
        return cls._lagrange_interpolation(0, list(x_s), list(y_s), cls.PRIME)

# Example Usage Helper
def generate_root_key() -> int:
    return secrets.randbelow(ShamirSecretSharing.PRIME)
