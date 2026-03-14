# fastmvc_media

File upload (multipart), image variants, and presigned URL helpers for FastMVC. Use with `fastmvc_storage` or any `IMediaStore` implementation.

## Upload

```python
from fastmvc_media import read_upload_as_bytes, validate_content_type, allowed_content_types

# In a FastAPI endpoint
@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    allowed = allowed_content_types()
    if not validate_content_type(file.content_type, allowed):
        raise HTTPException(400, "Unsupported file type")
    data = await read_upload_as_bytes(file, max_size=10 * 1024 * 1024)  # 10 MiB
    # Store via fastmvc_storage or IMediaStore
    result = store.upload(f"uploads/{file.filename}", data, content_type=file.content_type)
    return {"key": result.key, "url": result.url}
```

## Image variants

```pip install fastmvc_media[pillow]```

```python
from fastmvc_media import generate_image_variant

thumb_data = generate_image_variant(
    source_data,
    "webp",
    max_width=200,
    max_height=200,
    quality=80,
)
# Upload thumb_data to storage as e.g. thumbs/abc_200x200.webp
```

## Presigned URLs

Use `fastmvc_storage.build_storage_backend("s3")` and call `.presigned_url(key, expires_in=3600)` to serve private files via temporary URLs.
