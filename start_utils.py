"""
Startup utilities for CalCount: loads configuration, environment variables,
and initializes core services (DB, Redis, LLM, logging).
"""
import os
from typing import Any
from sqlalchemy.orm.session import Session
import redis
import sys

from dotenv import load_dotenv
from loguru import logger
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from configurations.cache import CacheConfiguration, CacheConfigurationDTO
from configurations.db import DBConfiguration, DBConfigurationDTO

from constants.default import Default


logger.remove(0)
logger.add(
    sys.stderr,
    colorize=True,
    format=(
        "<green>{time:MMMM-D-YYYY}</green> | <black>{time:HH:mm:ss}</black> | "
        "<level>{level}</level> | <cyan>{message}</cyan> | "
        "<magenta>{name}:{function}:{line}</magenta> | "
        "<yellow>{extra}</yellow>"
    ),
)

# Load environment variables from .env file
logger.info("Loading .env file and environment variables")
load_dotenv()

logger.info("Loading Configurations")
cache_configuration: CacheConfigurationDTO = CacheConfiguration().get_config()
db_configuration: DBConfigurationDTO = DBConfiguration().get_config()
logger.info("Loaded Configurations")

# Access environment variables
logger.info("Loading environment variables")
APP_NAME: str = os.environ.get("APP_NAME")
SECRET_KEY: str = os.getenv("SECRET_KEY")
ALGORITHM: str = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES: int = int(
    os.getenv(
        "ACCESS_TOKEN_EXPIRE_MINUTES",
        Default.ACCESS_TOKEN_EXPIRE_MINUTES,
    )
)
RATE_LIMIT_REQUESTS_PER_MINUTE: int = int(
    os.getenv(
        "RATE_LIMIT_REQUESTS_PER_MINUTE",
        Default.RATE_LIMIT_REQUESTS_PER_MINUTE,
    )
)
RATE_LIMIT_REQUESTS_PER_HOUR: int = int(
    os.getenv(
        "RATE_LIMIT_REQUESTS_PER_HOUR",
        Default.RATE_LIMIT_REQUESTS_PER_HOUR,
    )
)
RATE_LIMIT_WINDOW_SECONDS: int = int(
    os.getenv(
        "RATE_LIMIT_WINDOW_SECONDS",
        Default.RATE_LIMIT_WINDOW_SECONDS,
    )
)
RATE_LIMIT_BURST_LIMIT: int = int(
    os.getenv(
        "RATE_LIMIT_BURST_LIMIT",
        Default.RATE_LIMIT_BURST_LIMIT,
    )
)
logger.info("Loaded environment variables")

db_session: Session = None
if (
    db_configuration.user_name
    and db_configuration.password
    and db_configuration.host
    and db_configuration.port
    and db_configuration.database
    and db_configuration.connection_string
):
    logger.info("Initializing PostgreSQL database connection")
    engine = create_engine(
        db_configuration.connection_string.format(
            user_name=db_configuration.user_name,
            password=db_configuration.password,
            host=db_configuration.host,
            port=db_configuration.port,
            database=db_configuration.database,
        )
    )
    Session = sessionmaker[Session](bind=engine)
    db_session: Session = Session()
    logger.info("Initialized PostgreSQL database connection")

redis_session: redis.Redis = None
if (
    cache_configuration.host
    and cache_configuration.port
    and cache_configuration.password
):
    logger.info("Initializing Redis database connection")
    redis_session = redis.Redis(
        host=cache_configuration.host,
        port=cache_configuration.port,
        password=cache_configuration.password,
    )
    if not redis_session:
        logger.error("No Redis session available")
        raise RuntimeError("No Redis session available")
    logger.info("Initialized Redis database connection")

unprotected_routes: set = {
    "/health",
    "/user/login",
    "/user/register",
    "/docs",
    "/redoc",
}
callback_routes: set = set[Any]()

if db_session:  
    db_session.commit()
    logger.info("Database session committed and startup complete")
