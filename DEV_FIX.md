# Quick dev fix

This branch is intentionally failing the 80% coverage gate, so you can verify that `main` cannot receive an insufficiently tested change.

The task is isolated to `app/main.py` in `build_info`:

1. Replace the `label = "stable"` assignment inside `if debug:` with `label = "dev"`.
2. Add one test in `tests/test_api.py`:

```python
def test_debug_build_info() -> None:
    response = client.get("/api/build?debug=true")
    assert response.status_code == 200
    assert response.json() == {"label": "dev", "source": "branch"}
```

3. Run `pytest`. The test both verifies the bug fix and covers the endpoint, taking the suite above the 80% gate.

After the run is green, open a pull request from `dev` to `main`. The required GitHub checks will allow the merge only if coverage is at least 80%.
