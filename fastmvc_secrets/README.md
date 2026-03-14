# fastmvc_secrets

Secrets management for FastMVC: HashiCorp Vault, AWS Secrets Manager, GCP Secret Manager.

Config: `config/secrets/config.json` via `fastmvc_core.SecretsConfiguration`.

Optional: `pip install fastmvc_secrets[vault]`, `[aws]`, `[gcp]`.

```python
from fastmvc_secrets import build_secrets_backend

secrets = build_secrets_backend("vault")  # or "aws", "gcp"
if secrets:
    value = secrets.get_secret("app/database/password")
    secrets.set_secret("app/api_key", "sk-...")
```
