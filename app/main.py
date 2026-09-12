from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

app = FastAPI(title="FastAPI GitHub Template", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    """Small endpoint suitable for smoke checks and deployment probes."""
    return {"status": "ok"}


@app.get("/api/greet/{name}")
def greet(name: str, excited: bool = False) -> dict[str, str]:
    clean_name = name.strip()
    if not clean_name:
        raise HTTPException(status_code=400, detail="Name cannot be empty")
    suffix = "!" if excited else "."
    return {"message": f"Hello, {clean_name}{suffix}"}


@app.get("/api/build")
def build_info(debug: bool = False) -> dict[str, str]:
    """Temporary dev-only endpoint, deliberately left without test coverage."""
    label = "stable"
    source = "release"
    if debug:
        label = "stable"  # BUG: debug builds must be labelled "dev".
        source = "branch"
    return {"label": label, "source": source}


@app.get("/", response_class=HTMLResponse)
def home() -> str:
    return """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>FastAPI template</title><style>body{font-family:system-ui;max-width:680px;margin:12vh auto;padding:0 24px;color:#172033}code{background:#eef2ff;padding:3px 6px;border-radius:4px}</style></head>
<body><h1>FastAPI is ready</h1><p>A compact starter application for GitHub.</p><p>Check <code>/health</code> or call <code>/api/greet/World</code>.</p></body></html>"""
