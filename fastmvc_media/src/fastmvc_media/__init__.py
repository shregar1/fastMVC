"""
fastmvc_media – File upload, image variants, presigned URLs for FastMVC.
"""

from .abstractions import IMediaStore, IImageVariantGenerator, UploadResult
from .upload import read_upload_as_bytes, allowed_content_types, validate_content_type
from .variants import generate_image_variant

__version__ = "0.1.0"

__all__ = [
    "IMediaStore",
    "IImageVariantGenerator",
    "UploadResult",
    "read_upload_as_bytes",
    "allowed_content_types",
    "validate_content_type",
    "generate_image_variant",
]
