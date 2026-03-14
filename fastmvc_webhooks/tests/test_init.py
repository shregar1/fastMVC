"""Tests for fastmvc_webhooks."""

import pytest


def test_imports():
    from fastmvc_webhooks import (
        compute_signature,
        verify_signature,
        deliver_webhook,
        RetryPolicy,
    )
    assert compute_signature(b"test", "secret") is not None


def test_verify_roundtrip():
    from fastmvc_webhooks import compute_signature, verify_signature, signature_header_value

    payload = b'{"event":"test"}'
    secret = "sk_test"
    header = signature_header_value(payload, secret)
    assert verify_signature(payload, header, secret) is True
    assert verify_signature(payload, "sha256=wrong", secret) is False
