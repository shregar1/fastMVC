"""
fastmvc_admin – CRUD API for admin resources (users, roles, audit log) for FastMVC.
"""

from .abstractions import (
    AdminUserSummary,
    AdminRoleSummary,
    AuditLogEntry,
    IAdminUserRepository,
    IAdminRoleRepository,
    IAuditLogRepository,
)
from .router import get_admin_router

__version__ = "0.1.0"

__all__ = [
    "AdminUserSummary",
    "AdminRoleSummary",
    "AuditLogEntry",
    "IAdminUserRepository",
    "IAdminRoleRepository",
    "IAuditLogRepository",
    "get_admin_router",
]
