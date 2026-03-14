# Publish FastMVC on GitHub and Release

## 1. Publish the repo on GitHub

If the repo is not on GitHub yet:

### Option A: Create a new repository on GitHub

1. Go to [GitHub New Repository](https://github.com/new).
2. Set repository name (e.g. `fastmvc`).
3. Choose Public, add a description, **do not** initialize with README (you already have one).
4. Create the repository.

### Option B: Use GitHub CLI

```bash
cd /path/to/fastmvc
gh repo create fastmvc --public --source=. --remote=origin --push
```

### Add remote and push (if you created the repo in the UI)

From your **fastmvc** project root (the folder that contains `fast_mvc_main`, `fastmvc_core`, etc.):

```bash
cd /path/to/fastmvc

# If this folder is not yet a git repo, initialize and commit:
git init
git add .
git commit -m "Initial commit: FastMVC monorepo"

# Add GitHub as origin (replace with your repo URL)
git remote add origin https://github.com/YOUR_USERNAME/fastmvc.git
# or: git remote add origin git@github.com:YOUR_USERNAME/fastmvc.git

# Push (use main or master to match your default branch)
git branch -M main
git push -u origin main
```

---

## 2. Release (tag + GitHub Release + optional PyPI)

### One-time setup

- **PyPI**: Create project `pyfastmvc` on [pypi.org](https://pypi.org) and set up [Trusted Publishing](https://docs.pypi.org/trusted-publishers/) for the GitHub repo (recommended), or use an API token in `~/.pypirc` or `TWINE_PASSWORD`.
- **GitHub**: In the repo **Settings → Environments**, create environment `pypi` and add the PyPI trusted publisher (or secret for token).

### Run a release

1. **Set version** (e.g. `1.4.0`) in:
   - `fast_mvc_main/pyproject.toml` → `version = "1.4.0"`
   - `fast_mvc_main/fastmvc_cli/__init__.py` → `__version__ = "1.4.0"`
2. **Commit** the version bump and any release notes in `fast_mvc_main/CHANGELOG.md`.
3. **Run the release script** from the **repo root** (the `fastmvc` directory):

   ```bash
   # Tag and push only (no PyPI upload)
   VERSION=1.4.0 ./scripts/release_all.sh

   # Tag, push, and upload pyfastmvc to PyPI (if you use twine + token)
   VERSION=1.4.0 ./scripts/release_all.sh --pypi
   ```

4. **Create the GitHub Release**:
   - Open **Releases → Draft a new release**.
   - Choose tag `v1.4.0` (created by the script).
   - Title: `Release v1.4.0`.
   - Paste notes from `fast_mvc_main/CHANGELOG.md`.
   - Click **Publish release**.

If you use the included **GitHub Action** (`.github/workflows/release.yml`) and Trusted Publishing with PyPI, publishing the release will **automatically** build and publish the `pyfastmvc` package to PyPI. In that case you only need:

```bash
VERSION=1.4.0 ./scripts/release_all.sh
```

then create the release in the GitHub UI; no need for `--pypi` locally.

---

## 3. Summary

| Step | Action |
|------|--------|
| 1 | Create GitHub repo (or use `gh repo create`) |
| 2 | `git remote add origin ...` and `git push -u origin main` |
| 3 | Bump version in `fast_mvc_main` and commit |
| 4 | Run `VERSION=x.y.z ./scripts/release_all.sh` |
| 5 | On GitHub: Releases → New release → choose tag `vx.y.z` → Publish |
| 6 | PyPI publish happens via workflow (if configured) or with `--pypi` and twine |
