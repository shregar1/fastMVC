"""Unleash feature flags client."""

from __future__ import annotations

from typing import Any, Optional

from .base import IFeatureFlagsClient


class UnleashFeatureFlagsClient(IFeatureFlagsClient):
    """Unleash client wrapper."""

    def __init__(
        self,
        url: str,
        app_name: str = "fastmvc",
        instance_id: str = "fastmvc-instance",
        api_key: Optional[str] = None,
    ):
        try:
            from UnleashClient import UnleashClient
        except ImportError as e:
            raise RuntimeError("UnleashClient required. Install: pip install fastmvc_feature_flags[unleash]") from e
        self._client = UnleashClient(
            url=url,
            app_name=app_name,
            instance_id=instance_id,
            custom_headers={"Authorization": api_key} if api_key else None,
        )
        self._client.initialize_client()

    def is_enabled(self, flag_key: str, context: Optional[dict[str, Any]] = None) -> bool:
        return self._client.is_enabled(flag_key, context or {})

    def get_value(self, flag_key: str, context: Optional[dict[str, Any]] = None) -> Any:
        return self._client.get_variant(flag_key, context or {})
