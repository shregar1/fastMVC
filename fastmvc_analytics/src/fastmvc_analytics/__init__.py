"""
fastmvc_analytics – Analytics and event tracking for FastMVC.
"""

from fastmvc_core import AnalyticsConfiguration, AnalyticsConfigurationDTO

from .base import IAnalyticsBackend, build_analytics_client

__version__ = "0.1.0"

__all__ = [
    "IAnalyticsBackend",
    "AnalyticsConfiguration",
    "AnalyticsConfigurationDTO",
    "build_analytics_client",
]
