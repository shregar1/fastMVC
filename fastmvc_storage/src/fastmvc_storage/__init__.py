"""
fastmvc_storage – Object storage (S3, GCS, Azure Blob, local) for FastMVC.
"""

from fastmvc_core import StorageConfiguration, StorageConfigurationDTO

from .base import IStorageBackend, build_storage_backend
from .local_backend import LocalStorageBackend

__version__ = "0.1.0"

__all__ = [
    "IStorageBackend",
    "LocalStorageBackend",
    "StorageConfiguration",
    "StorageConfigurationDTO",
    "build_storage_backend",
]
