# uHOME Server Quickstart

This quickstart gets the local runtime running and validates the first Wizard
and Empire handoff seams.

## Prerequisites

- Python 3.9+
- Git
- optional sibling repos for the paired flow: `../uDOS-wizard` and `../uHOME-empire`

## 1. Bootstrap And Validate

From the repo root:

```bash
bash scripts/run-uhome-server-checks.sh
source .venv/bin/activate
```

The check script creates `.venv` when needed, installs the editable dev
dependencies, and runs the current `pytest` suite.

## 2. Run The API

```bash
source .venv/bin/activate
python -m uvicorn uhome_server.app:app --host 127.0.0.1 --port 8000 --reload
```

Default URL:

- `http://127.0.0.1:8000`

## 3. Smoke Test Core Routes

In another terminal:

```bash
curl http://127.0.0.1:8000/api/health
curl http://127.0.0.1:8000/api/runtime/ready
curl http://127.0.0.1:8000/api/runtime/info
curl http://127.0.0.1:8000/api/household/status
curl http://127.0.0.1:8000/api/launcher/status
```

Open the thin automation status view in a browser:

- `http://127.0.0.1:8000/api/runtime/thin/automation`

## 4. Pair Wizard To The Running Server

From the sibling `uDOS-wizard` repo:

```bash
python3 -m pip install --upgrade pip
python3 -m pip install -e .
UHOME_SERVER_URL=http://127.0.0.1:8000 python3 -m wizard.main
```

Then verify the bridge from another terminal:

```bash
curl http://127.0.0.1:8787/uhome/bridge/status
curl http://127.0.0.1:8787/uhome/automation/status
```

If both repos are checked out side by side, `udos-wizard-demo` from
`uDOS-wizard` also launches the paired stack automatically.

## 5. Dispatch An Empire Pack Into The Live Runtime

From the sibling `uHOME-empire` repo:

```bash
bash scripts/run-empire-checks.sh
python3 scripts/smoke/pack_preview.py --json --pack quickstart --execution-brief
python3 scripts/smoke/pack_run.py --json --pack quickstart --uhome-url http://127.0.0.1:8000 --write-default-report
```

Use `uHOME-empire/docs/quickstart.md` for the live Wizard and automation
bridge probes after the local runtime is up.

## 6. Useful CLI Commands

```bash
source .venv/bin/activate
uhome launcher status
uhome contracts sync-record
uhome backup list
```

## Next Docs

- `docs/getting-started.md` for the repo entry sequence
- `FIRST-TIME-INSTALL.md` for clean-machine setup
- `docs/DEPLOYMENT-GUIDE.md` for Ubuntu service deployment
- `docs/operations/README.md` for runbooks and operational recovery
