# fastmvc_webhooks

Webhook signing (HMAC) and outbound delivery with retries for FastMVC (Stripe-style).

## Verifying incoming webhooks

```python
from fastmvc_webhooks import verify_signature

# In your endpoint: read body as bytes, get header X-Webhook-Signature
valid = verify_signature(body, request.headers.get("X-Webhook-Signature", ""), secret="whsec_...")
if not valid:
    raise HTTPException(401, "Invalid signature")
```

## Sending webhooks

```python
from fastmvc_webhooks import deliver_webhook, RetryPolicy
import json

payload = json.dumps({"event": "order.created", "id": "123"}).encode()
status, err = await deliver_webhook(
    "https://customer.com/webhook",
    payload,
    secret="whsec_...",
    retry_policy=RetryPolicy(max_attempts=3, initial_delay_seconds=1, backoff_factor=2),
)
```
