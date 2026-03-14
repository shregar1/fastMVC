# fastmvc_tenancy

Multi-tenancy for FastMVC: tenant context (contextvars), resolvers (header, subdomain, path, JWT), and middleware.

## Usage

```python
from fastmvc_tenancy import (
    Tenant, TenantConfig, InMemoryTenantStore,
    get_current_tenant, TenantContext,
    TenantMiddleware, HeaderTenantResolver,
)

store = InMemoryTenantStore()
# ... register tenants with store.create(Tenant(...))

resolver = HeaderTenantResolver(store, "X-Tenant-ID")
app.add_middleware(TenantMiddleware, resolver=resolver, required=True)

# In services
tenant = get_current_tenant()
# scope DB/queries by tenant.id
```

## JWT

Use `JWTTenantResolver(store, claim_name="tenant_id")` when the tenant ID is in the authenticated user (e.g. from JWT). Ensure auth middleware runs first and sets `request.state.user` with a `tenant_id` attribute.
