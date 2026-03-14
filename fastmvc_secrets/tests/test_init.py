"""Tests for fastmvc_secrets."""

import pytest


def test_imports():
    from fastmvc_secrets import (
        ISecretsBackend,
        SecretsConfiguration,
        SecretsConfigurationDTO,
        build_secrets_backend,
    )
    assert build_secrets_backend is not None
