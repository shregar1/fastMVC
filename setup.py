"""
FastMVC - Production-grade MVC Framework for FastAPI.

This setup.py configures FastMVC as a pip-installable package
with a CLI entry point for generating new projects.

Usage:
    $ pip install .
    $ fastmvc generate my_project
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README for long description
readme_path = Path(__file__).parent / "README.md"
long_description = ""
if readme_path.exists():
    long_description = readme_path.read_text(encoding="utf-8")

# Read requirements
requirements_path = Path(__file__).parent / "requirements.txt"
requirements = []
if requirements_path.exists():
    requirements = [
        line.strip()
        for line in requirements_path.read_text().splitlines()
        if line.strip() and not line.startswith("#")
    ]

setup(
    name="fastmvc",
    version="1.0.0",
    author="FastMVC Team",
    author_email="team@fastmvc.dev",
    description="Production-grade MVC Framework for FastAPI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fastmvc/fastmvc",
    project_urls={
        "Bug Tracker": "https://github.com/fastmvc/fastmvc/issues",
        "Documentation": "https://fastmvc.dev/docs",
        "Source Code": "https://github.com/fastmvc/fastmvc",
    },
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Framework :: FastAPI",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Typing :: Typed",
    ],
    keywords="fastapi, mvc, framework, api, rest, web, backend, python",
    packages=find_packages(exclude=["tests", "tests.*", "htmlcov"]),
    python_requires=">=3.10",
    install_requires=[
        "click>=8.0.0",
        "fastapi>=0.100.0",
        "uvicorn>=0.20.0",
        "pydantic>=2.0.0",
        "sqlalchemy>=2.0.0",
        "python-dotenv>=1.0.0",
        "loguru>=0.7.0",
        "pyjwt>=2.8.0",
        "bcrypt>=4.0.0",
        "redis>=4.0.0",
        "psycopg2-binary>=2.9.0",
        "email-validator>=2.0.0",
        "ulid>=1.1",
        "httpx>=0.24.0",
    ],
    extras_require={
        "dev": [
            "pytest>=8.0.0",
            "pytest-asyncio>=0.21.0",
            "pytest-cov>=4.0.0",
            "pytest-mock>=3.10.0",
            "coverage>=7.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "fastmvc=fastmvc_cli.cli:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
