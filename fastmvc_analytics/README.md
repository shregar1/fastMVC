# fastmvc_analytics

Analytics and event tracking for FastMVC. Uses HTTP sink from config or optional Segment/PostHog/Mixpanel.

Config: `config/analytics/config.json` via `fastmvc_core.AnalyticsConfiguration`.

```python
from fastmvc_analytics import build_analytics_client

analytics = build_analytics_client()
if analytics:
    analytics.track("user-123", "purchase", {"amount": 99})
    analytics.identify("user-123", {"email": "u@example.com"})
```
