"""
Database engine and session factory.

Creates SQLAlchemy engine and session from fastmvc_core DBConfiguration.
The application should call create_and_set_session() at startup (or create_engine +
create_session + set_global_session), then use get_db_session() or DBDependency.
"""

from typing import Optional

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

from fastmvc_core import DBConfiguration, DBConfigurationDTO


_global_session: Optional[Session] = None
_engine: Optional[Engine] = None


def get_engine(config: Optional[DBConfigurationDTO] = None) -> Engine:
    """
    Build a SQLAlchemy Engine from DB configuration.

    Args:
        config: Database config DTO. If None, uses DBConfiguration().get_config().

    Returns:
        SQLAlchemy Engine.

    Raises:
        RuntimeError: If config is incomplete.
    """
    if config is None:
        config = DBConfiguration().get_config()
    if not (
        config.user_name
        and config.password
        and config.host
        and config.port
        and config.database
        and config.connection_string
    ):
        raise RuntimeError(
            "Database configuration is incomplete. "
            "Set user_name, password, host, port, database, and connection_string."
        )
    url = config.connection_string.format(
        user_name=config.user_name,
        password=config.password,
        host=config.host,
        port=config.port,
        database=config.database,
    )
    return create_engine(url)


def create_session_factory(engine: Engine) -> sessionmaker:
    """Create a sessionmaker bound to the given engine."""
    return sessionmaker[Session](bind=engine)


def set_global_session(session: Session) -> None:
    """Set the global session used by get_db_session() and DBDependency."""
    global _global_session
    _global_session = session


def set_global_engine(engine: Engine) -> None:
    """Store engine reference (optional, for cleanup)."""
    global _engine
    _engine = engine


def get_db_session() -> Optional[Session]:
    """Return the global database session, or None if not initialized."""
    return _global_session


def create_and_set_session(config: Optional[DBConfigurationDTO] = None) -> Optional[Session]:
    """
    Create engine and session from config, set as global, and return the session.
    Returns None if config is incomplete (no session created).
    """
    if config is None:
        config = DBConfiguration().get_config()
    if not (
        config.user_name
        and config.password
        and config.host
        and config.port
        and config.database
        and config.connection_string
    ):
        return None
    eng = get_engine(config)
    set_global_engine(eng)
    factory = create_session_factory(eng)
    session: Session = factory()
    set_global_session(session)
    return session
