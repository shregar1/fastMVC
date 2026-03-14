# fastmvc_feature_flags

Feature flags for FastMVC: LaunchDarkly, Unleash.

Config: `config/feature_flags/config.json` via `fastmvc_core.FeatureFlagsConfiguration`.

Optional: `pip install fastmvc_feature_flags[launchdarkly]` or `[unleash]`.

```python
from fastmvc_feature_flags import build_feature_flags_client

flags = build_feature_flags_client()
if flags:
    if flags.is_enabled("new-checkout", context={"key": "user-123"}):
        ...
    value = flags.get_value("pricing-tier", context={"key": "user-123"})
```
