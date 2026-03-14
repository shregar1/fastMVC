# fastmvc_admin

Admin CRUD API for FastMVC: users, roles, audit log. Provide your own repository implementations and mount the optional router.

## Usage

```python
from fastmvc_admin import get_admin_router, IAdminUserRepository, IAuditLogRepository

# Implement IAdminUserRepository, IAdminRoleRepository, IAuditLogRepository
# (backed by your DB)

router = get_admin_router(
    user_repo=my_user_repo,
    role_repo=my_role_repo,
    audit_repo=my_audit_repo,
    prefix="/admin",
)
app.include_router(router)
# Protect /admin/* with your auth (e.g. require admin role)
```

Endpoints: `GET/PATCH /admin/users`, `GET/PUT /admin/users/{id}/roles`, `GET /admin/roles`, `GET /admin/audit`.
