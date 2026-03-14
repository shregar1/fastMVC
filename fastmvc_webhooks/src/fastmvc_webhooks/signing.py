"""
Webhook payload signing (HMAC) for verification and outbound headers.
"""

import hashlib
import hmac
from typing import Optional


def compute_signature(payload: bytes, secret: str, algorithm: str = "sha256") -> str:
    """
    Compute HMAC signature for payload (e.g. for X-Webhook-Signature header).

    Args:
        payload: Raw body bytes.
        secret: Shared secret.
        algorithm: Hash name (sha256, sha384, sha512).

    Returns:
        Hex-encoded signature.
    """
    digest = hashlib.new(algorithm)
    sig = hmac.new(
        secret.encode("utf-8") if isinstance(secret, str) else secret,
        payload,
        digest,
    ).hexdigest()
    return sig


def verify_signature(
    payload: bytes,
    signature_header: str,
    secret: str,
    *,
    prefix: str = "sha256=",
    algorithm: str = "sha256",
) -> bool:
    """
    Verify incoming webhook signature (e.g. Stripe-style "sha256=...").

    Args:
        payload: Raw request body.
        signature_header: Value of X-Webhook-Signature (or similar).
        secret: Shared secret.
        prefix: Expected prefix (e.g. "sha256="); the rest is the hex signature.
        algorithm: Hash algorithm.

    Returns:
        True if signature matches.
    """
    if not signature_header.startswith(prefix):
        return False
    expected = compute_signature(payload, secret, algorithm=algorithm)
    received = signature_header[len(prefix) :].strip()
    return hmac.compare_digest(expected, received)


def signature_header_value(payload: bytes, secret: str, algorithm: str = "sha256") -> str:
    """Produce header value for outbound webhook (e.g. X-Webhook-Signature: sha256=...)."""
    sig = compute_signature(payload, secret, algorithm=algorithm)
    return f"{algorithm}=" + sig
