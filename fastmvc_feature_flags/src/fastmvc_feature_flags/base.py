"""
Feature flags client interface and factory.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Optional

from fastmvc_core import FeatureFlagsConfiguration


class IFeatureFlagsClient(ABC):
    """Interface for feature flag clients."""

    @abstractmethod
    def is_enabled(self, flag_key: str, context: Optional[dict[str, Any]] = None) -> bool:
        """Return True if the feature flag is enabled for the given context."""
        raise NotImplementedError

    @abstractmethod
    def get_value(self, flag_key: str, context: Optional[dict[str, Any]] = None) -> Any:
        """Return the flag value (e.g. string, number, JSON)."""
        raise NotImplementedError


def build_feature_flags_client() -> Optional[IFeatureFlagsClient]:
    """
    Build a feature flags client from FeatureFlagsConfiguration (config/feature_flags/config.json).
    Prefers LaunchDarkly, then Unleash.
    """
    cfg = FeatureFlagsConfiguration().get_config()

    if getattr(cfg.launchdarkly, "enabled", False) and cfg.launchdarkly.sdk_key:
        try:
            from .launchdarkly_client import LaunchDarklyFeatureFlagsClient
            return LaunchDarklyFeatureFlagsClient(
                sdk_key=cfg.launchdarkly.sdk_key,
                default_user_key=getattr(cfg.launchdarkly, "default_user_key", "anonymous"),
            )
        except ImportError:
            pass

    if getattr(cfg.unleash, "enabled", False) and cfg.unleash.url:
        try:
            from .unleash_client import UnleashFeatureFlagsClient
            return UnleashFeatureFlagsClient(
                url=cfg.unleash.url,
                app_name=cfg.unleash.app_name,
                instance_id=cfg.unleash.instance_id,
                api_key=cfg.unleash.api_key,
            )
        except ImportError:
            pass

    return None
