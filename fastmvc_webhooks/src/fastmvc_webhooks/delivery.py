"""
Outbound webhook delivery with retries and optional signing.
"""

import asyncio
import time
from dataclasses import dataclass, field
from typing import Any, Callable, Optional

import httpx

from .signing import signature_header_value


@dataclass
class RetryPolicy:
    """Retry policy for failed deliveries."""

    max_attempts: int = 3
    initial_delay_seconds: float = 1.0
    backoff_factor: float = 2.0
    retry_on_status: set[int] = field(default_factory=lambda: {408, 429, 500, 502, 503})


async def deliver_webhook(
    url: str,
    payload: bytes,
    *,
    secret: Optional[str] = None,
    signature_header_name: str = "X-Webhook-Signature",
    extra_headers: Optional[dict[str, str]] = None,
    retry_policy: Optional[RetryPolicy] = None,
    timeout: float = 30.0,
) -> tuple[int, Optional[str]]:
    """
    POST payload to url with optional HMAC signature and retries.

    Returns:
        (status_code, error_message). error_message is None on success.
    """
    policy = retry_policy or RetryPolicy()
    headers = dict(extra_headers or {})
    headers["Content-Type"] = "application/json"
    if secret:
        headers[signature_header_name] = signature_header_value(payload, secret)

    last_status: int = 0
    last_error: Optional[str] = None
    delay = policy.initial_delay_seconds

    for attempt in range(policy.max_attempts):
        try:
            async with httpx.AsyncClient(timeout=timeout) as client:
                r = await client.post(url, content=payload, headers=headers)
            last_status = r.status_code
            if 200 <= r.status_code < 300:
                return (r.status_code, None)
            if r.status_code not in policy.retry_on_status:
                return (r.status_code, f"HTTP {r.status_code}: {r.text[:200]}")
            last_error = f"HTTP {r.status_code}: {r.text[:200]}"
        except Exception as e:
            last_error = str(e)
            last_status = 0

        if attempt < policy.max_attempts - 1:
            await asyncio.sleep(delay)
            delay *= policy.backoff_factor

    return (last_status, last_error)


def deliver_webhook_sync(
    url: str,
    payload: bytes,
    *,
    secret: Optional[str] = None,
    signature_header_name: str = "X-Webhook-Signature",
    extra_headers: Optional[dict[str, str]] = None,
    retry_policy: Optional[RetryPolicy] = None,
    timeout: float = 30.0,
) -> tuple[int, Optional[str]]:
    """Synchronous wrapper for deliver_webhook."""
    import asyncio
    return asyncio.get_event_loop().run_until_complete(
        deliver_webhook(
            url,
            payload,
            secret=secret,
            signature_header_name=signature_header_name,
            extra_headers=extra_headers,
            retry_policy=retry_policy,
            timeout=timeout,
        )
    )
