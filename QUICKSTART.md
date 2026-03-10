# uHOME Server Quickstart

This quickstart gets the API running locally in about 5 minutes.

## Prerequisites

- Python 3.9+
- Git

## 1. Install

```bash
git clone https://github.com/fredporter/uHOME-server.git
cd uHOME-server
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
python -m pip install -e '.[dev]'
```

## 2. Run The API

```bash
source .venv/bin/activate
python -m uvicorn uhome_server.app:app --reload
```

Default URL:

- `http://localhost:8000`

## 3. Smoke Test

In another terminal:

```bash
curl http://localhost:8000/api/health
curl http://localhost:8000/api/runtime/ready
curl http://localhost:8000/api/household/status
```

## 4. Run Tests

```bash
source .venv/bin/activate
pytest tests/
```

## 5. Useful CLI Commands

```bash
source .venv/bin/activate
uhome launcher status
uhome backup list
```

## Next Docs

- `FIRST-TIME-INSTALL.md` for clean-machine setup
- `docs/DEPLOYMENT-GUIDE.md` for Ubuntu service deployment
- `docs/operations/README.md` for runbooks and operational recovery
