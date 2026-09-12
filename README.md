# FastAPI GitHub template

Minimal FastAPI starter with a page, health probe, tests, coverage gate, and GitHub Actions.

## Run locally

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/`.

## Tests

```powershell
pytest --no-cov tests/test_smoke.py -q  # 2 fast smoke checks
pytest                                  # 30 cases: 22 passed, 8 expected failures
```

The eight unfinished cases use `xfail`: they are reported as not passing but do not break CI. The coverage gate is `73%` (`--cov-fail-under=73`). When those cases are implemented, remove their `xfail` marker.

The workflow in `.github/workflows/ci.yml` runs smoke checks first, then the full suite with the coverage threshold on every pull request and push to `main`.
