# fastmvc_search

Search backends for FastMVC: Meilisearch, Typesense, OpenSearch.

Config: `config/search/config.json` via `fastmvc_core.SearchConfiguration`.

Optional: `pip install fastmvc_search[meilisearch]`, `[typesense]`, `[opensearch]`.

```python
from fastmvc_search import build_search_backend

search = build_search_backend("meilisearch")
if search:
    search.index_documents("products", [{"id": "1", "title": "Widget"}])
    hits = search.search("products", "widget", limit=10)
```
