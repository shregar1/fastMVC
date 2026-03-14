"""
fastmvc_feature_flags – Feature flags (LaunchDarkly, Unleash) for FastMVC.
"""

from fastmvc_core import FeatureFlagsConfiguration, FeatureFlagsConfigurationDTO

from .base import IFeatureFlagsClient, build_feature_flags_client

__version__ = "0.1.0"

__all__ = [
    "IFeatureFlagsClient",
    "FeatureFlagsConfiguration",
    "FeatureFlagsConfigurationDTO",
    "build_feature_flags_client",
]
