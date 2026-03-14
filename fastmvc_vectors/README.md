# fastmvc_vectors

Vector stores for FastMVC: Pinecone, Qdrant, Weaviate. Config from `fastmvc_core.VectorsConfiguration` (`config/vectors/config.json`).

Optional: `pip install fastmvc_vectors[pinecone]`, `[qdrant]`, `[weaviate]`.

```python
from fastmvc_vectors import build_vector_store

store = build_vector_store("pinecone")
if store:
    store.upsert("docs", [("id1", [0.1, 0.2], {"title": "Doc"})])
    hits = store.query("docs", [0.1, 0.2], top_k=5)
```
