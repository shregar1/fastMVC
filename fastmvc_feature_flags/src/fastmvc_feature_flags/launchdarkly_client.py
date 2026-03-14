"""LaunchDarkly feature flags client."""

from __future__ import annotations

from typing import Any, Optional

from .base import IFeatureFlagsClient


class LaunchDarklyFeatureFlagsClient(IFeatureFlagsClient):
    """LaunchDarkly SDK wrapper."""

    def __init__(self, sdk_key: str, default_user_key: str = "anonymous"):
        try:
            import launchdarkly.server_sdk as ld
        except ImportError as e:
            raise RuntimeError("launchdarkly-server-sdk required. Install: pip install fastmvc_feature_flags[launchdarkly]") from e
        self._sdk_key = sdk_key
        self._default_key = default_user_key
        self._client = ld.LDClient(sdk_key)
        self._client.wait_for_initialization()

    def _user(self, context: Optional[dict[str, Any]] = None) -> dict[str, Any]:
        if not context:
            return {"key": self._default_key}
        key = context.get("key") or context.get("user_key") or self._default_key
        return {"key": key, **{k: v for k, v in context.items() if k not in ("key", "user_key")}}

    def is_enabled(self, flag_key: str, context: Optional[dict[str, Any]] = None) -> bool:
        return self._client.variation(flag_key, self._user(context), False)

    def get_value(self, flag_key: str, context: Optional[dict[str, Any]] = None) -> Any:
        return self._client.variation(flag_key, self._user(context), None)
