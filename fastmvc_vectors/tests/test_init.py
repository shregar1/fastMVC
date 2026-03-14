"""Tests for fastmvc_vectors."""

import pytest


def test_imports():
    from fastmvc_vectors import (
        IVectorStore,
        VectorsConfiguration,
        VectorsConfigurationDTO,
        build_vector_store,
    )
    assert build_vector_store is not None
