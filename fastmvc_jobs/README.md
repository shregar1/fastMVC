# fastmvc_jobs

Background jobs for FastMVC: Celery, RQ, Dramatiq.

Uses `fastmvc_core` for configuration (`config/jobs/config.json`).

## Celery

```bash
pip install fastmvc_jobs[celery]
```

```python
from fastmvc_jobs import make_celery_app, get_celery_app_if_enabled

app = make_celery_app()  # from config/jobs/config.json

@app.task
def send_welcome_email(user_id: int):
    ...

# Or only if enabled in config
app = get_celery_app_if_enabled()
if app:
    app.worker_main(argv=["worker", "--loglevel=info"])
```

Run worker: `celery -A your_app.celery_app:app worker --loglevel=info` (after binding `app` in your app module).
