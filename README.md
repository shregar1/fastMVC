# FastMVC

Monorepo for the FastMVC ecosystem: CLI (pyfastmvc), core config, and optional packages (db, payments, identity, queues, jobs, storage, etc.).

## Quick start

- **CLI and main app**: [fast_mvc_main/README.md](fast_mvc_main/README.md)
- **Core config**: [fastmvc_core/](fastmvc_core/)
- **Install all packages locally**: `./install_packages.sh`

## Publish on GitHub and release

See **[RELEASE.md](RELEASE.md)** for:

1. Pushing this repo to GitHub (new repo or existing remote)
2. Creating a release (tag, GitHub Release, and optional PyPI publish) using `scripts/release_all.sh`

## Repository layout

| Path | Description |
|------|-------------|
| `fast_mvc_main/` | Main app template + CLI (`pyfastmvc`) |
| `fastmvc_core/` | Config, DTOs, loaders |
| `fastmvc_db/` | SQLAlchemy engine, session, DBDependency |
| `fastmvc_*` | Optional packages (payments, identity, queues, jobs, storage, etc.) |
| `scripts/release_all.sh` | Tag, push, and optional PyPI publish |
| `.github/workflows/release.yml` | Publish to PyPI on GitHub Release |
