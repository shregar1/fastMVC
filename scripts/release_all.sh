#!/usr/bin/env bash
# Release FastMVC: tag, push, and optionally create GitHub release.
# Usage:
#   VERSION=1.4.0 ./scripts/release_all.sh          # tag and push
#   VERSION=1.4.0 ./scripts/release_all.sh --pypi   # also build and publish pyfastmvc to PyPI (requires twine/uv and token)
set -e

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

VERSION="${VERSION:-}"
if [ -z "$VERSION" ]; then
  echo "Usage: VERSION=x.y.z $0 [--pypi]"
  echo "  --pypi  Also build and upload pyfastmvc to PyPI (requires TWINE_USERNAME/TWINE_PASSWORD or .pypirc)"
  exit 1
fi

TAG="v${VERSION}"
BRANCH="${BRANCH:-main}"
PUBLISH_PYPI=false
for arg in "$@"; do
  [ "$arg" = "--pypi" ] && PUBLISH_PYPI=true
done

echo "→ Releasing FastMVC $VERSION (tag: $TAG, branch: $BRANCH)"
echo ""

# 1. Ensure clean state (optional; comment out if you want to allow dirty)
if ! git diff-index --quiet HEAD -- 2>/dev/null; then
  echo "⚠ Working tree has uncommitted changes. Commit or stash them first."
  read -r -p "Continue anyway? [y/N] " ans
  [ "$ans" != "y" ] && [ "$ans" != "Y" ] && exit 1
fi

# 2. Sync version in fast_mvc_main (optional; uncomment to auto-bump)
# sed -i.bak "s/version = \".*\"/version = \"$VERSION\"/" fast_mvc_main/pyproject.toml
# sed -i.bak "s/__version__ = \".*\"/__version__ = \"$VERSION\"/" fast_mvc_main/fastmvc_cli/__init__.py

# 3. Run tests (optional; uncomment if you have tests at repo root)
# python -m pytest fast_mvc_main/tests -v --tb=short || exit 1

# 4. Tag
if git rev-parse "$TAG" >/dev/null 2>&1; then
  echo "Tag $TAG already exists. Delete with: git tag -d $TAG"
  exit 1
fi
git tag -a "$TAG" -m "Release $TAG"
echo "✓ Tagged $TAG"

# 5. Push branch and tag
echo "→ Pushing branch and tag..."
git push origin "$BRANCH"
git push origin "$TAG"
echo "✓ Pushed $BRANCH and $TAG"

# 6. Optional: build and publish pyfastmvc to PyPI
if [ "$PUBLISH_PYPI" = true ]; then
  echo ""
  echo "→ Building and publishing pyfastmvc to PyPI..."
  (cd fast_mvc_main && python -m pip install -q build twine && python -m build && twine upload dist/*)
  echo "✓ Published pyfastmvc $VERSION to PyPI"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✓ Release $TAG done."
echo ""
echo "Next: Create a GitHub Release from the tag:"
echo "  1. Open: https://github.com/YOUR_ORG/fastmvc/releases/new?tag=$TAG"
echo "  2. Set title to: Release $TAG"
echo "  3. Paste release notes from CHANGELOG.md"
echo "  4. Publish release"
echo ""
echo "If you use GitHub Actions with Trusted Publishing, publishing the release will trigger the workflow to upload to PyPI."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
