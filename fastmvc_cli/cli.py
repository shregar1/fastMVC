"""
FastMVC CLI - Command Line Interface.

This module provides the main CLI entry point for FastMVC framework.
It uses Click for building the command-line interface.

Commands:
    generate: Create a new FastMVC project from template
    version: Display the current FastMVC version
    info: Display information about FastMVC

Example:
    $ fastmvc generate my_api
    $ fastmvc version
    $ fastmvc info
"""

import click
import sys
from pathlib import Path

from fastmvc_cli import __version__
from fastmvc_cli.generator import ProjectGenerator


@click.group()
@click.version_option(version=__version__, prog_name="fastmvc")
def cli():
    """
    FastMVC - Production-grade MVC Framework for FastAPI.
    
    Generate new FastAPI projects with a clean MVC architecture,
    built-in authentication, rate limiting, security headers,
    and comprehensive documentation.
    
    \b
    Quick Start:
        $ fastmvc generate my_project
        $ cd my_project
        $ pip install -r requirements.txt
        $ python -m uvicorn app:app --reload
    """
    pass


@cli.command()
@click.argument("project_name")
@click.option(
    "--output-dir", "-o",
    default=".",
    help="Directory where the project will be created (default: current directory)"
)
@click.option(
    "--git/--no-git",
    default=True,
    help="Initialize a git repository (default: True)"
)
@click.option(
    "--venv/--no-venv",
    default=False,
    help="Create a virtual environment (default: False)"
)
@click.option(
    "--install/--no-install",
    default=False,
    help="Install dependencies after generation (default: False)"
)
def generate(project_name: str, output_dir: str, git: bool, venv: bool, install: bool):
    """
    Generate a new FastMVC project.
    
    Creates a new FastAPI project with the FastMVC architecture pattern,
    including all necessary directories, configuration files, and boilerplate code.
    
    \b
    Arguments:
        PROJECT_NAME: Name of the new project (will be used as directory name)
    
    \b
    Examples:
        $ fastmvc generate my_api
        $ fastmvc generate my_api --output-dir ~/projects
        $ fastmvc generate my_api --git --venv --install
    """
    click.echo()
    click.secho("╔══════════════════════════════════════════════════════════════╗", fg="cyan")
    click.secho("║                                                              ║", fg="cyan")
    click.secho("║   ███████╗ █████╗ ███████╗████████╗███╗   ███╗██╗   ██╗ ██████╗║", fg="cyan")
    click.secho("║   ██╔════╝██╔══██╗██╔════╝╚══██╔══╝████╗ ████║██║   ██║██╔════╝║", fg="cyan")
    click.secho("║   █████╗  ███████║███████╗   ██║   ██╔████╔██║██║   ██║██║     ║", fg="cyan")
    click.secho("║   ██╔══╝  ██╔══██║╚════██║   ██║   ██║╚██╔╝██║╚██╗ ██╔╝██║     ║", fg="cyan")
    click.secho("║   ██║     ██║  ██║███████║   ██║   ██║ ╚═╝ ██║ ╚████╔╝ ╚██████╗║", fg="cyan")
    click.secho("║   ╚═╝     ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝     ╚═╝  ╚═══╝   ╚═════╝║", fg="cyan")
    click.secho("║                                                              ║", fg="cyan")
    click.secho("║          Production-grade MVC Framework for FastAPI          ║", fg="cyan")
    click.secho("╚══════════════════════════════════════════════════════════════╝", fg="cyan")
    click.echo()
    
    # Validate project name
    if not project_name.replace("_", "").replace("-", "").isalnum():
        click.secho(
            f"✗ Invalid project name: '{project_name}'. "
            "Use only letters, numbers, underscores, and hyphens.",
            fg="red"
        )
        sys.exit(1)
    
    # Create generator and run
    generator = ProjectGenerator(
        project_name=project_name,
        output_dir=output_dir,
        init_git=git,
        create_venv=venv,
        install_deps=install
    )
    
    try:
        generator.generate()
        click.echo()
        click.secho("✓ Project generated successfully!", fg="green", bold=True)
        click.echo()
        click.secho("Next steps:", fg="yellow", bold=True)
        click.echo()
        click.echo(f"  1. cd {project_name}")
        click.echo("  2. pip install -r requirements.txt")
        click.echo("  3. cp .env.example .env  # Configure your environment")
        click.echo("  4. docker-compose up -d  # Start PostgreSQL and Redis")
        click.echo("  5. python -m uvicorn app:app --reload")
        click.echo()
        click.secho(f"  → Your API will be available at http://localhost:8000", fg="cyan")
        click.secho(f"  → API docs at http://localhost:8000/docs", fg="cyan")
        click.echo()
    except Exception as e:
        click.secho(f"✗ Error generating project: {e}", fg="red")
        sys.exit(1)


@cli.command()
def info():
    """
    Display information about FastMVC.
    
    Shows details about the framework including version,
    features, and documentation links.
    """
    click.echo()
    click.secho("FastMVC Framework", fg="cyan", bold=True)
    click.secho("=" * 40, fg="cyan")
    click.echo()
    click.echo(f"  Version:     {__version__}")
    click.echo(f"  Python:      {sys.version.split()[0]}")
    click.echo()
    click.secho("Features:", fg="yellow", bold=True)
    click.echo("  • MVC Architecture Pattern")
    click.echo("  • Built-in Authentication (JWT)")
    click.echo("  • Rate Limiting Middleware")
    click.echo("  • Security Headers Middleware")
    click.echo("  • Request Context Tracking")
    click.echo("  • Input Validation & Sanitization")
    click.echo("  • Comprehensive Test Suite")
    click.echo("  • Production-grade Documentation")
    click.echo()
    click.secho("Project Structure:", fg="yellow", bold=True)
    click.echo("  • abstractions/   - Base interfaces & contracts")
    click.echo("  • configurations/ - Config loaders")
    click.echo("  • constants/      - Application constants")
    click.echo("  • controllers/    - Request handlers")
    click.echo("  • dependencies/   - Dependency injection")
    click.echo("  • dtos/           - Data transfer objects")
    click.echo("  • errors/         - Custom exceptions")
    click.echo("  • middlewares/    - Request/Response middleware")
    click.echo("  • models/         - Database models")
    click.echo("  • repositories/   - Data access layer")
    click.echo("  • services/       - Business logic")
    click.echo("  • utilities/      - Helper functions")
    click.echo()


@cli.command()
def version():
    """Display the FastMVC version."""
    click.echo(f"FastMVC v{__version__}")


def main():
    """Main entry point for the CLI."""
    cli()


if __name__ == "__main__":
    main()

