# uHOME Server

uHOME Server is the local-network home infrastructure pathway for `uDOS`.

This repository owns the Linux-first server runtime for household media,
automation, launcher, and dashboard surfaces. It stays separate from `uDOS`
core and `uDOS-sonic`: `uDOS` owns the shared runtime and contracts,
`uDOS-sonic` owns deployment and hardware bootstrap, and `uHOME-server` owns
the home infrastructure runtime, examples, and pathway documentation.

## Quick Start

If you already have Python 3.9+ installed, this is the fastest way to run the API:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
python -m pip install -e '.[dev]'
python -m uvicorn uhome_server.app:app --reload
```

In a second terminal:

```bash
curl http://localhost:8000/api/health
```

For a dedicated quick path, see `QUICKSTART.md`.
For first-time machine setup, see `FIRST-TIME-INSTALL.md`.

## Pathway Contract

Each repo in the family should answer the same questions in the same order.

1. What pathway does this repo provide?
   `uHOME-server` provides the local-network home infrastructure pathway for
   `uDOS`.
2. What Markdown or vault surfaces does it read or write?
   Education-facing household examples live under `vault/`. The active runtime
   still bootstraps local state under `memory/`.
3. What services does it expose?
   The server currently exposes Home Assistant, platform, runtime, library,
   containers, network, and dashboard APIs.
4. What modules are optional?
   The current module families are media, DVR, home operations, Steam surface,
   and Home Assistant bridge.
5. How does it connect back to `uDOS` core?
   Through shared contracts, workspace defaults, compatible install bundles, and
   downstream client/server integration.

## Repository Layout

- `src/uhome_server/` active Python package and API/CLI entrypoints
- `apps/` education-facing map of dashboard and kiosk surfaces
- `modules/` capability-family map for home features
- `services/` runtime service map for playback, scheduling, launcher, LAN
  discovery, and bridge work
- `vault/` Markdown-first sample household state
- `courses/` student-facing learning path scaffold
- `config/` stable checked-in configuration lane for the refactor
- `scripts/linux/` Linux-side operational script lane
- `examples/installer/` installer bundle and probe examples
- `docs/` architecture, pathway, client, and implementation docs
- `tests/` focused coverage for the standalone runtime

Phase 1 note:

- the live runtime remains in `src/uhome_server/`
- the new top-level roots are an information-architecture scaffold first
- no big-bang code move is required to use the repo today

See `docs/architecture/PHASE-1-IA-MAP.md` for the current-to-target mapping.
See `docs/architecture/ROOT-POLICY.md` for canonical vs transitional root
status.

## Entry Points

### Use

Start here if you want to run or operate the current server:

- `QUICKSTART.md` for a 5-minute local run path
- `FIRST-TIME-INSTALL.md` for first-time setup on a clean machine
- `README.md` for runtime overview and commands
- `docs/pathway/USE.md` for the current operator path
- `examples/installer/` for standalone and dual-boot bundle examples

### Learn

Start here if you want to understand the pathway model:

- `courses/` for the student-facing learning scaffold
- `vault/` for Markdown-first household examples
- `docs/pathway/README.md` for the repo's role in the wider `uDOS` family

### Build

Start here if you want to extend the repo or work on the refactor:

- `docs/architecture/UHOME-SERVER-DEV-PLAN.md` for the active repo-local
  development plan
- `docs/uHOME-server-dev-brief.md` and
  `docs/uHOME-server-education-dev-brief.md` for the two governing local briefs
- `docs/README.md` for the maintainer-facing index
- `docs/architecture/PHASE-1-IA-MAP.md` for current-to-target ownership
- `docs/pathway/REPO-FAMILY.md` for `uDOS` / `uHOME` / `uDOS-sonic` boundary rules
- `src/uhome_server/` for the active implementation package

## Current Runtime

The server bootstraps local runtime directories under `memory/` on startup and
uses `memory/config/uhome.json` as the canonical local config file, with legacy
fallback to `memory/config/wizard.json` during migration.

Current API surfaces:

- `/api/ha/*` for the Home Assistant bridge
- `/api/platform/uhome/*` for presentation status and control
- `/api/runtime/*` for runtime info and readiness checks
- `/api/library/*` for cloned library repo management
- `/api/containers/*` for manifest-driven container clone and launch status
- `/api/network/*` for decentralized node and storage registry state
- `/api/dashboard/*` for aggregated server health and summary state

Operator CLI entrypoints:

```bash
uhome launcher status
uhome-launcher start --presentation thin-gui
uhome-installer preflight --probe ./probe.json
uhome-installer plan --bundle-dir ./bundle --probe ./probe.json --output ./install-plan.json
uhome-installer stage --bundle-dir ./bundle --probe ./probe.json --stage-dir ./stage
uhome-installer execute-stage --stage-dir ./stage --target-root ./target-root
uhome-installer apply-target --target-root ./target-root --host-root ./host-root
uhome-installer verify-target --host-root ./host-root
uhome-installer health-check-target --host-root ./host-root
uhome-installer apply-live --host-root ./host-root
uhome-installer apply-live --host-root ./host-root --execute
uhome-installer rollback-target --host-root ./host-root
```

## Development

Use Python 3.9 or newer. Create a virtual environment, upgrade the local
packaging tools, then install the package in editable mode:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip setuptools wheel
.venv/bin/python -m pip install -e '.[dev]'
```

Run the API with uvicorn:

```bash
.venv/bin/python -m uvicorn uhome_server.app:app --reload
```

Run the current local test suite with:

```bash
.venv/bin/python -m pytest
```

The installer flow still materializes Linux-oriented target assets and
host-promotion plans from the active Python package. That deployment machinery
is transitional and documented in the Phase 1 mapping doc so boundary cleanup
can continue without breaking the current runtime.

## License

This project is released under the MIT License. See `LICENSE`.
