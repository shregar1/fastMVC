"""
fastmvc_llm – LLM provider abstraction (OpenAI, Anthropic, Ollama) for FastMVC.
"""

from fastmvc_core import LLMConfiguration, LLMConfigurationDTO
from fastmvc_core.services.llm import (
    ILLMService,
    OpenAILLMService,
    AnthropicLLMService,
    OllamaLLMService,
    build_llm_service,
)

__version__ = "0.1.0"

__all__ = [
    "ILLMService",
    "OpenAILLMService",
    "AnthropicLLMService",
    "OllamaLLMService",
    "build_llm_service",
    "LLMConfiguration",
    "LLMConfigurationDTO",
]
