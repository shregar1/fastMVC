"""
Search backend interface and factory.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, List, Optional

from fastmvc_core import SearchConfiguration


class ISearchBackend(ABC):
    """Interface for search backends (Meilisearch, Typesense, OpenSearch)."""

    name: str

    @abstractmethod
    def index_documents(self, index_name: str, documents: List[dict[str, Any]]) -> None:
        """Index or upsert documents."""
        raise NotImplementedError

    @abstractmethod
    def search(
        self,
        index_name: str,
        query: str,
        *,
        limit: int = 20,
        offset: int = 0,
        filter: Optional[dict[str, Any]] = None,
    ) -> List[dict[str, Any]]:
        """Search and return list of hits."""
        raise NotImplementedError

    @abstractmethod
    def delete_index(self, index_name: str) -> None:
        """Delete an index."""
        raise NotImplementedError


def build_search_backend(backend: str = "meilisearch") -> Optional[ISearchBackend]:
    """
    Build a search backend from SearchConfiguration (config/search/config.json).
    backend: "meilisearch" | "typesense" | "opensearch"
    """
    cfg = SearchConfiguration().get_config()

    if backend == "meilisearch" and getattr(cfg.meilisearch, "enabled", False) and cfg.meilisearch.url:
        try:
            from .meilisearch_backend import MeilisearchBackend
            return MeilisearchBackend(
                url=cfg.meilisearch.url,
                api_key=cfg.meilisearch.api_key,
            )
        except ImportError:
            return None

    if backend == "typesense" and getattr(cfg.typesense, "enabled", False):
        try:
            from .typesense_backend import TypesenseBackend
            return TypesenseBackend(
                host=cfg.typesense.host,
                port=cfg.typesense.port,
                protocol=cfg.typesense.protocol,
                api_key=cfg.typesense.api_key,
            )
        except ImportError:
            return None

    if backend == "opensearch" and getattr(cfg.opensearch, "enabled", False) and cfg.opensearch.hosts:
        try:
            from .opensearch_backend import OpenSearchBackend
            return OpenSearchBackend(
                hosts=cfg.opensearch.hosts,
                username=cfg.opensearch.username,
                password=cfg.opensearch.password,
            )
        except ImportError:
            return None

    return None
