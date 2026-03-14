"""
fastmvc_identity – Identity provider abstractions and builders for FastMVC.
"""

from fastmvc_core import IdentityProvidersConfiguration, IdentityProvidersConfigurationDTO

from .providers import (
    IdentityUserProfile,
    IIdentityProvider,
    build_identity_providers,
)

__version__ = "0.1.0"

__all__ = [
    "IdentityUserProfile",
    "IIdentityProvider",
    "IdentityProvidersConfiguration",
    "IdentityProvidersConfigurationDTO",
    "build_identity_providers",
]
