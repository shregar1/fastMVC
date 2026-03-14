"""Tests for fastmvc_media."""

import pytest


def test_imports():
    from fastmvc_media import (
        IMediaStore,
        UploadResult,
        read_upload_as_bytes,
        generate_image_variant,
        validate_content_type,
    )
    assert validate_content_type("image/jpeg", ["image/jpeg"]) is True
    assert validate_content_type("image/svg+xml", ["image/jpeg"]) is False
