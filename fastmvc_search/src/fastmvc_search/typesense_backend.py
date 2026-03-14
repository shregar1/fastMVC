"""Typesense backend."""

from __future__ import annotations

from typing import Any, List, Optional

from .base import ISearchBackend


class TypesenseBackend(ISearchBackend):
    """Typesense client wrapper."""

    name = "typesense"

    def __init__(
        self,
        host: str = "localhost",
        port: int = 8108,
        protocol: str = "http",
        api_key: Optional[str] = None,
    ):
        try:
            from typesense import Client
        except ImportError as e:
            raise RuntimeError("typesense required. Install: pip install fastmvc_search[typesense]") from e
        self._client = Client({
            "nodes": [{"host": host, "port": str(port), "protocol": protocol}],
            "api_key": api_key or "xyz",
            "connection_timeout_seconds": 2,
        })

    def index_documents(self, index_name: str, documents: List[dict[str, Any]]) -> None:
        for d in documents:
            self._client.collections[index_name].documents.upsert(d)

    def search(
        self,
        index_name: str,
        query: str,
        *,
        limit: int = 20,
        offset: int = 0,
        filter: Optional[dict[str, Any]] = None,
    ) -> List[dict[str, Any]]:
        r = self._client.collections[index_name].documents.search({
            "q": query,
            "per_page": limit,
            "page": (offset // limit) + 1 if limit else 1,
            "filter_by": _filter_str(filter) if filter else None,
        })
        return [h["document"] for h in r.get("hits", [])]

    def delete_index(self, index_name: str) -> None:
        self._client.collections[index_name].delete()


def _filter_str(f: dict[str, Any]) -> str:
    return " && ".join(f"{k}:{v}" for k, v in f.items())
