"""Tests for fastmvc_admin."""

import pytest


def test_imports():
    from fastmvc_admin import (
        AdminUserSummary,
        AuditLogEntry,
        IAdminUserRepository,
        get_admin_router,
    )
    assert get_admin_router is not None
