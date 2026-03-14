"""
fastmvc_search – Search backends (Meilisearch, Typesense, OpenSearch) for FastMVC.
"""

from fastmvc_core import SearchConfiguration, SearchConfigurationDTO

from .base import ISearchBackend, build_search_backend

__version__ = "0.1.0"

__all__ = [
    "ISearchBackend",
    "SearchConfiguration",
    "SearchConfigurationDTO",
    "build_search_backend",
]
