# uHOME-server

## Purpose

Always-on Linux-based uHOME runtime for persistent local-network services,
scheduling, Steam-server host duties, and local vault viewing or unlock
surfaces.

## Ownership

- local-network services
- persistent scheduling
- service modules
- home and server infrastructure surfaces
- Linux-side Steam server host runtime
- local Vault Reader and Beacon Activate offline-library surfaces

## Non-Goals

- canonical runtime semantics
- shell ownership
- provider bridge ownership
- Google or HubSpot sync orchestration owned by `uHOME-empire`
- Apple or iCloud sync ownership owned by the macOS desktop app

## Spine

- `services/`
- `scheduling/`
- `modules/`
- `docs/`
- `tests/`
- `scripts/`
- `config/`

## Local Development

Build service modules as explicit, testable units and keep managed state outside the repo.

## Family Relation

`uHOME-server` provides the always-on local runtime. It complements
`uDOS-core`, pairs with `uDOS-wizard` for local networking contracts, and
leaves Google or HubSpot sync workflows to `uHOME-empire`.

## Transitional Runtime Note

The existing standalone runtime and installer flow remain in `src/uhome_server/` and related legacy-support roots such as `apps/`, `courses/`, `defaults/`, `examples/`, `library/`, `memory/`, and `vault/`.

This preserves the pre-existing remote history while the repo converges on the v2 scaffold and boundary model.

## Quick Start

```bash
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip setuptools wheel
.venv/bin/python -m pip install -e '.[dev]'
.venv/bin/python -m uvicorn uhome_server.app:app --reload
```

In another terminal:

```bash
curl http://localhost:8000/api/health
```

For machine setup and operational details, see `QUICKSTART.md`, `FIRST-TIME-INSTALL.md`, and the legacy documentation preserved under `docs/`.

## Activation

The v2 repo activation path is documented in `docs/activation.md`.

Run the current repo validation entrypoint with:

```bash
scripts/run-uhome-server-checks.sh
```
