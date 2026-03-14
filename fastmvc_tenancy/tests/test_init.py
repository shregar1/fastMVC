"""Tests for fastmvc_tenancy."""

import pytest


def test_imports():
    from fastmvc_tenancy import (
        Tenant,
        TenantConfig,
        get_current_tenant,
        TenantMiddleware,
        HeaderTenantResolver,
        InMemoryTenantStore,
    )
    assert Tenant is not None
    assert get_current_tenant is not None
