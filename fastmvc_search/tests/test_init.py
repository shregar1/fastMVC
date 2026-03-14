"""Tests for fastmvc_search."""

import pytest


def test_imports():
    from fastmvc_search import (
        ISearchBackend,
        SearchConfiguration,
        SearchConfigurationDTO,
        build_search_backend,
    )
    assert build_search_backend is not None
