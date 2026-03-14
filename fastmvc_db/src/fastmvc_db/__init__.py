"""
fastmvc_db – DB extension for FastMVC.

Provides SQLAlchemy engine/session from fastmvc_core DB config,
FastAPI DBDependency, table name constants, and get_database_url for Alembic.
"""

from .dependency import DBDependency
from .engine import (
    create_and_set_session,
    create_session_factory,
    get_db_session,
    get_engine,
    set_global_session,
)
from .table import Table
from .url import get_database_url

__version__ = "0.1.0"

__all__ = [
    "__version__",
    "DBDependency",
    "Table",
    "create_and_set_session",
    "create_session_factory",
    "get_database_url",
    "get_db_session",
    "get_engine",
    "set_global_session",
]
