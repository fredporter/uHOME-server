# uHOME-server

## Purpose

Always-on local-network runtime for persistent services, scheduling, and home/server modules.

## Ownership

- local-network services
- persistent scheduling
- service modules
- home and server infrastructure surfaces

## Non-Goals

- canonical runtime semantics
- shell ownership
- provider bridge ownership

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

uHOME-server provides persistent local services that complement Core and Wizard.

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
