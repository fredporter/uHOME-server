# uHOME-server

## Purpose

Linux-based `uHOME` service stream for persistent household services,
scheduling, Steam-server host duties, and ThinUI/local console surfaces built
on the wider runtime spine.

## Ownership

- local-network services
- persistent scheduling
- automation fulfillment
- service modules
- home and server infrastructure surfaces
- Linux-side Steam server host runtime
- Thin GUI and kiosk-style local presentation shells
- local Vault Reader and Beacon Activate offline-library surfaces

## Non-Goals

- canonical runtime semantics
- shell ownership
- provider bridge ownership
- primary always-on uDOS command-centre ownership
- primary browser-GUI ownership
- Google or HubSpot sync orchestration owned by `uDOS-empire`
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
Use `QUICKSTART.md` for the first runnable path and use
`examples/basic-uhome-server-session.md` for the smallest standalone smoke.

## Family Relation

`uHOME-server` is now the `uHOME` service lane rather than the primary
definition of the family runtime spine.

The intended family direction is:

- `uDOS-ubuntu` hosts the base always-on command centre
- `uHOME-server` provides household services and local console/ThinUI flows on
  top of that runtime
- `uDOS-wizard` provides publishing, provider, MCP, and assist adapters
- `uDOS-empire` handles selected external sync and publishing extensions

The v2 split is explicit:

- `uHOME-server` owns the base runtime, scheduling, household services, and
  persistent local execution
- `uHOME-server` owns Thin GUI and kiosk-style local presentation contracts
- `uDOS-wizard` owns workflow authority, online assist, and the browser
  operator GUI
- `uHOME-matter` owns Matter, Home Assistant, and local automation extension
  contracts
- `uHOME-client` and app repos consume runtime contracts without taking over
  server ownership

## Transitional Runtime Note

The existing standalone runtime and installer flow remain in `src/uhome_server/` and related legacy-support roots such as `apps/`, `courses/`, `defaults/`, `examples/`, `library/`, `memory/`, and `vault/`.

This preserves the pre-existing remote history while the repo converges on the v2 scaffold and boundary model.

For the base/runtime boundary itself, see `docs/base-runtime-boundary.md`.

## Quick Start

```bash
bash scripts/run-uhome-server-checks.sh
.venv/bin/python -m uvicorn uhome_server.app:app --host 127.0.0.1 --port 8000 --reload
```

For the direct local console/kiosk launch path, use:

```bash
bash scripts/first-run-launch.sh
```

That bootstraps the repo, starts `uHOME-server`, activates the default local
presentation lane, and opens the console surface at
`http://127.0.0.1:8000/api/runtime/thin/automation`.

On macOS, the Finder wrapper is:

```bash
open ./scripts/first-run-launch.command
```

In another terminal:

```bash
curl http://localhost:8000/api/health
curl http://localhost:8000/api/runtime/ready
```

For the full runtime, Wizard pairing, and Empire bridge path, see
`QUICKSTART.md`, `FIRST-TIME-INSTALL.md`, and the legacy documentation
preserved under `docs/`.

For operator env vars and preflight host checks, use
`docs/ENVIRONMENT-CONFIGURATION.md` and `bash scripts/check-prereqs.sh`.

## Activation

The v2 repo activation path is documented in `docs/activation.md`.

Run the current repo validation entrypoint with:

```bash
bash scripts/run-uhome-server-checks.sh
```

Shared sync-record contract tooling is also available through:

```bash
uhome contracts sync-record
uhome contracts validate-sync-record --input path/to/envelope.json
```

Runtime ingest and retrieval surfaces are available at:

```bash
POST /api/runtime/sync-records/ingest
GET /api/runtime/sync-records/latest
GET /api/runtime/sync-records
```

Wizard-owned household networking policy consumption surfaces are available at:

```bash
GET /api/runtime/contracts/uhome-network-policy
POST /api/runtime/contracts/uhome-network-policy/validate
```
