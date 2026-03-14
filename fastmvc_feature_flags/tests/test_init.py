"""Tests for fastmvc_feature_flags."""

import pytest


def test_imports():
    from fastmvc_feature_flags import (
        IFeatureFlagsClient,
        FeatureFlagsConfiguration,
        FeatureFlagsConfigurationDTO,
        build_feature_flags_client,
    )
    assert build_feature_flags_client is not None
