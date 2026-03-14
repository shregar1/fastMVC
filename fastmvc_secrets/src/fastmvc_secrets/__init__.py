"""
fastmvc_secrets – Secrets backends (Vault, AWS, GCP) for FastMVC.
"""

from fastmvc_core import SecretsConfiguration, SecretsConfigurationDTO

from .base import ISecretsBackend, build_secrets_backend

__version__ = "0.1.0"

__all__ = [
    "ISecretsBackend",
    "SecretsConfiguration",
    "SecretsConfigurationDTO",
    "build_secrets_backend",
]
