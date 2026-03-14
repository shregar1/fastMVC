"""Meilisearch backend."""

from __future__ import annotations

from typing import Any, List, Optional

from .base import ISearchBackend


class MeilisearchBackend(ISearchBackend):
    """Meilisearch client wrapper."""

    name = "meilisearch"

    def __init__(self, url: str, api_key: Optional[str] = None):
        try:
            from meilisearch import Client
        except ImportError as e:
            raise RuntimeError("meilisearch required. Install: pip install fastmvc_search[meilisearch]") from e
        self._client = Client(url, api_key)

    def index_documents(self, index_name: str, documents: List[dict[str, Any]]) -> None:
        index = self._client.index(index_name)
        index.add_documents(documents)

    def search(
        self,
        index_name: str,
        query: str,
        *,
        limit: int = 20,
        offset: int = 0,
        filter: Optional[dict[str, Any]] = None,
    ) -> List[dict[str, Any]]:
        index = self._client.index(index_name)
        r = index.search(query, limit=limit, offset=offset, filter=filter)
        return [h for h in r.get("hits", [])]

    def delete_index(self, index_name: str) -> None:
        self._client.delete_index(index_name)
