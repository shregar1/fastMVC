"""Smoke test package import."""

def test_import():
    import fastmvc_identity as i
    assert i.build_identity_providers is not None
    assert i.IIdentityProvider is not None
    assert i.IdentityUserProfile is not None
    assert i.IdentityProvidersConfiguration is not None
