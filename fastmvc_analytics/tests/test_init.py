"""Tests for fastmvc_analytics."""

import pytest


def test_imports():
    from fastmvc_analytics import (
        IAnalyticsBackend,
        AnalyticsConfiguration,
        AnalyticsConfigurationDTO,
        build_analytics_client,
    )
    assert build_analytics_client is not None
