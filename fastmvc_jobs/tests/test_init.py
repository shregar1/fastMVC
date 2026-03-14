"""Tests for fastmvc_jobs."""

import pytest


def test_imports():
    from fastmvc_jobs import (
        JobsConfiguration,
        JobsConfigurationDTO,
        make_celery_app,
        get_celery_app_if_enabled,
    )
    assert make_celery_app is not None
    assert JobsConfiguration is not None
