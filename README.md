# FastAPI CI/CD starter

<p align="center">
  <b>A minimal web application with a protected quality gate.</b>
</p>

<p align="center">
  <a href="../../actions/workflows/ci.yml"><img src="../../actions/workflows/ci.yml/badge.svg" alt="CI status"></a>
  <img src="https://img.shields.io/badge/coverage%20gate-80%25-00a86b?style=flat-square" alt="Coverage gate: 80%">
  <img src="https://img.shields.io/badge/python-3.12-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.12">
  <img src="https://img.shields.io/badge/FastAPI-0.115%2B-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI">
</p>

> **Coverage rule:** code from `dev` can be merged into `main` only after CI reports **80% or higher** coverage.

## What is included

| Area | Included |
| --- | --- |
| Web application | Page at `/`, health probe at `/health`, greeting API at `/api/greet/{name}` |
| Smoke checks | Two fast endpoint checks |
| Test suite | 30 cases: 22 passing and 8 explicitly expected failures (`xfail`) |
| Quality gate | `pytest-cov` requires at least **80%** coverage |
| Automation | GitHub Actions runs checks on `dev`, `main`, and pull requests to `main` |

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

The eight unfinished cases use `xfail`: they are reported as not passing but do not break CI. The coverage gate is `80%` (`--cov-fail-under=80`). When those cases are implemented, remove their `xfail` marker.

## CI/CD flow

```text
dev branch  ->  pull request to main  ->  smoke tests  ->  full tests + coverage >= 80%  ->  merge
```

The workflow in `.github/workflows/ci.yml` runs smoke checks first, then the full suite with the coverage threshold. The `main` branch is protected by these required checks.
