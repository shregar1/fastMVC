"""OpenSearch backend."""

from __future__ import annotations

from typing import Any, List, Optional

from .base import ISearchBackend


class OpenSearchBackend(ISearchBackend):
    """OpenSearch client wrapper."""

    name = "opensearch"

    def __init__(
        self,
        hosts: List[str],
        username: Optional[str] = None,
        password: Optional[str] = None,
    ):
        try:
            from opensearchpy import OpenSearch
        except ImportError as e:
            raise RuntimeError("opensearch-py required. Install: pip install fastmvc_search[opensearch]") from e
        self._client = OpenSearch(
            hosts=hosts,
            http_auth=(username, password) if username and password else None,
            use_ssl="https" in (hosts or ["http://localhost"])[0],
            verify_certs=True,
        )

    def index_documents(self, index_name: str, documents: List[dict[str, Any]]) -> None:
        for i, d in enumerate(documents):
            doc_id = d.get("id") or str(i)
            self._client.index(index=index_name, body=d, id=doc_id, refresh=True)

    def search(
        self,
        index_name: str,
        query: str,
        *,
        limit: int = 20,
        offset: int = 0,
        filter: Optional[dict[str, Any]] = None,
    ) -> List[dict[str, Any]]:
        body: dict[str, Any] = {
            "query": {"simple_query_string": {"query": query}},
            "from": offset,
            "size": limit,
        }
        if filter:
            body["query"] = {"bool": {"must": [body["query"], {"term": filter}]}}
        r = self._client.search(index=index_name, body=body)
        return [h["_source"] for h in r.get("hits", {}).get("hits", [])]

    def delete_index(self, index_name: str) -> None:
        self._client.indices.delete(index=index_name)
