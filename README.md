# GitHub Actions CI Demo (FastAPI)

This project demonstrates a simple CI pipeline using **GitHub Actions** to run unit tests for a FastAPI app.

---

## 🧪 What It Does

- ✅ Runs tests on every `push` and `pull request`
- ✅ Uses Python 3.11 environment
- ✅ Installs dependencies from `requirements.txt`
- ✅ Tests FastAPI endpoint via `pytest`

---

## 🚀 Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## 🧪 Run Tests

```bash
pytest tests/
```

---

## 🔄 CI Pipeline

The workflow lives in `.github/workflows/ci.yml` and does the following:
- Checks out code
- Sets up Python
- Installs dependencies
- Runs tests

---

## 🐳 Docker (Optional)

```bash
docker build -t fastapi-ci-demo .
docker run -p 8000:8000 fastapi-ci-demo
```

---

## 🏁 Result

You’ll see test results in GitHub on every commit. Great starting point for real-world CI/CD.
