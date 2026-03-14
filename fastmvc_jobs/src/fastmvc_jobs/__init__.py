"""
fastmvc_jobs – Background jobs (Celery, RQ, Dramatiq) for FastMVC.
"""

from fastmvc_core import JobsConfiguration, JobsConfigurationDTO

from .celery_app import get_celery_app_if_enabled, make_celery_app

__version__ = "0.1.0"

__all__ = [
    "JobsConfiguration",
    "JobsConfigurationDTO",
    "make_celery_app",
    "get_celery_app_if_enabled",
]
