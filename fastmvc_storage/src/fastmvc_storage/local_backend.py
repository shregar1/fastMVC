"""Local filesystem storage backend."""

from __future__ import annotations

import os
from pathlib import Path
from typing import BinaryIO, Optional

from .base import IStorageBackend


class LocalStorageBackend(IStorageBackend):
    """Store objects on local disk."""

    name = "local"

    def __init__(self, base_dir: str = "storage", base_url: Optional[str] = None):
        self._base = Path(base_dir)
        self._base_url = base_url or ""

    def upload(
        self,
        key: str,
        body: bytes | BinaryIO,
        *,
        content_type: Optional[str] = None,
        metadata: Optional[dict[str, str]] = None,
    ) -> str:
        path = self._base / key
        path.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(body, bytes):
            path.write_bytes(body)
        else:
            path.write_bytes(body.read())
        return self._base_url.rstrip("/") + "/" + key if self._base_url else str(path)

    def download(self, key: str) -> bytes:
        path = self._base / key
        return path.read_bytes()

    def delete(self, key: str) -> None:
        path = self._base / key
        if path.exists():
            path.unlink()
