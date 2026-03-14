# fastmvc_storage

Object storage for FastMVC: S3, GCS, Azure Blob, local filesystem.

Config: `config/storage/config.json` via `fastmvc_core.StorageConfiguration`.

Optional: `pip install fastmvc_storage[s3]`, `[gcs]`, `[azure]`.

```python
from fastmvc_storage import build_storage_backend

store = build_storage_backend("s3")  # or "gcs", "azure_blob", "local"
if store:
    store.upload("docs/readme.txt", b"content", content_type="text/plain")
    url = store.presigned_url("docs/readme.txt", expires_in=3600)
```
