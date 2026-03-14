"""Tests for fastmvc_storage."""

import pytest


def test_imports():
    from fastmvc_storage import (
        IStorageBackend,
        LocalStorageBackend,
        StorageConfiguration,
        StorageConfigurationDTO,
        build_storage_backend,
    )
    assert LocalStorageBackend is not None
    assert build_storage_backend is not None
