"""Tests for fastmvc_llm."""

import pytest


def test_imports():
    from fastmvc_llm import (
        ILLMService,
        build_llm_service,
        LLMConfiguration,
        LLMConfigurationDTO,
    )
    assert build_llm_service is not None
