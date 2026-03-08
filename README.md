# uHOME Server

uHOME Server is the standalone local-first home-media and home-operations
server extracted from the `uDOS` home profile lane.

This repository is the Linux side of `uHOME`: the standalone Steam-server and
home-operations host that can run by itself or participate in a dual-boot
deployment where Windows 10 is present as an auxiliary gaming layer.

## Migrated Scope

- Home Assistant bridge routes and command handlers
- `uHOME` presentation status/start/stop routes
- file-backed DVR scheduling, playback handoff, and ad-processing settings
- Sonic-side `uHOME` bundle, preflight, and install-plan contracts
- canonical v1.5 `uHOME` specs and decision docs

## Deployment Model

- primary runtime target: Linux `uHOME Server`
- valid standalone mode: Linux Steam-server without any Windows partition
- valid dual-boot mode: Linux `uHOME Server` plus Windows 10 gaming layer
- valid client surfaces: Android tablet, Google TV, and Apple TV style LAN
  clients over separate app repos
- LAN topology may include multiple satellite-style Steam servers so household
  playback and launcher capacity can stay available when a more powerful
  dual-boot machine is offline for dedicated Windows gaming
- the media library may span multiple interconnected drives, partitions, and
  server nodes that appear or disappear over time without collapsing the whole
  household lane

## Repository Layout

- `src/uhome_server/` standalone service and install-plan code
- `defaults/workspace/` migrated workspace seed defaults for `uHOME`
- `tests/` focused coverage for migrated routes and Sonic contracts
- `library/` git-backed library manifests and cloned runtime support
- `docs/specs/` implementation-facing specifications
- `docs/decisions/` architecture and product decisions
- `docs/services/` migrated service-level operational docs
- `docs/ui/` dashboard and client-surface contracts
- `docs/workspace/` migrated workspace templates and instructions

## Development

Install the package and dev dependencies, then run the API with uvicorn:

```bash
python3 -m pip install -e '.[dev]'
python3 -m uvicorn uhome_server.app:app --reload
```

The server bootstraps its local runtime directories under `memory/` on startup
and now uses `memory/config/uhome.json` as the canonical local config file,
with legacy fallback to `memory/config/wizard.json` during migration.

The API exposes:

- `/api/ha/*` for the Home Assistant bridge
- `/api/platform/uhome/*` for presentation status/control
- `/api/runtime/*` for runtime info and startup/readiness checks
- `/api/library/*` for cloned library repo management
- `/api/containers/*` for manifest-driven container clone/launch status
- `/api/network/*` for decentralized node and storage-volume registry state
- `/api/dashboard/*` for aggregated `uHOME` dashboard health and summary state

Run the current local test suite with:

```bash
python3 -m pytest
```

Operator CLI entrypoints are also available:

```bash
uhome launcher status
uhome-launcher start --presentation thin-gui
uhome-installer preflight --probe ./probe.json
uhome-installer plan --bundle-dir ./bundle --probe ./probe.json --output ./install-plan.json
uhome-installer stage --bundle-dir ./bundle --probe ./probe.json --stage-dir ./stage
uhome-installer execute-stage --stage-dir ./stage --target-root ./target-root
uhome-installer apply-target --target-root ./target-root --host-root ./host-root
uhome-installer verify-target --host-root ./host-root
uhome-installer rollback-target --host-root ./host-root
```

`execute-stage` writes Linux-oriented deployment assets into the target root,
including environment files under `etc/uhome/`, systemd unit files under
`systemd/system/`, target wants links, receipts, state, and a
`bin/systemctl-apply.sh` helper for host-side enable/start orchestration.

`apply-target` promotes those generated assets into a host-style filesystem
layout under the chosen host root and snapshots the previous state for
`rollback-target`. It also writes a `systemctl` command plan and verification
report under `var/lib/uhome/`, plus a health-check plan and upgrade diff based
on prior receipts.

Example installer probes and verifiable sample bundles live under
`examples/installer/`, including standalone Linux and dual-boot reference
bundles.

## License

This project is released under the MIT License. See `LICENSE`.
