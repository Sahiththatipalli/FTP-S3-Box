def is_dry_run_enabled():
    import os
    return os.getenv("DRY_RUN", "false").lower() == "true"
