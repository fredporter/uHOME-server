# Phase 1 Information Architecture Map

Status: complete
Scope: education-facing repo scaffold without runtime relocation

## Goal

Align `uHOME-server` with the shared uDOS v2 family language:

- `apps/`
- `modules/`
- `services/`
- `vault/`
- `docs/`
- `courses/`
- `scripts/`
- `config/`
- `tests/`

The live Python package remains rooted at `src/uhome_server/` during this
phase.

## No-Break Policy

- keep the active package layout under `src/uhome_server/`
- keep `pyproject.toml` entrypoints unchanged
- keep `examples/installer/` and existing tests working
- treat new top-level roots as canonical teaching and documentation entrypoints
  first

## Current-To-Target Map

| Current surface | Phase 1 target surface | Owner | Notes |
| --- | --- | --- | --- |
| `src/uhome_server/routes/dashboard.py` and `docs/ui/UHOME-DASHBOARD.md` | `apps/dashboard/` | `uHOME-server` | Server summary contract stays in `src/` for now. |
| `src/uhome_server/routes/platform.py` and `src/uhome_server/services/uhome_presentation_service.py` | `apps/tablet-kiosk/`, `modules/steam-surface/`, `services/launcher/` | `uHOME-server` | Presentation control remains server-owned. |
| `src/uhome_server/services/home_assistant/`, `src/uhome_server/services/home_assistant_service.py`, and `src/uhome_server/routes/home_assistant.py` | `modules/home-assistant-bridge/` and `services/bridge/` | `uHOME-server` | Clear module plus service split already exists. |
| `src/uhome_server/cluster/registry.py` and `src/uhome_server/routes/network.py` | `services/lan-discovery/` | `uHOME-server` | File-backed LAN contract is now explicit; durable identity and orchestration remain future work. |
| `src/uhome_server/services/uhome_command_handlers.py`, `src/uhome_server/routes/library.py`, and `src/uhome_server/routes/containers.py` | `modules/media/` and `services/playback/` | `uHOME-server` | Playback and media surfaces need cleaner service separation later. |
| file-backed DVR scheduling and future jobs | `modules/dvr/` and `services/scheduling/` | `uHOME-server` | Durable scheduling backend remains future work. |
| `defaults/workspace/` | `config/` support lane | shared with `uDOS-core` and `uDOS-shell` | Keep workspace compatibility while the checked-in config root grows. |
| `examples/installer/` and `src/uhome_server/installer/bundle.py` | transitional install-contract lane | `uHOME-server` | `uHOME`-specific bundle contracts stay here while the public installer boundary settles. |
| `library/` | module/runtime support surface | `uHOME-server` | Keep as a runtime support root until a cleaner module ownership split is ready. |

## Repo Family Boundary

### `uDOS-core`

Owns:

- core runtime
- shared contracts
- family-wide education framing

### `uDOS-shell` and `uDOS-wizard`

Own:

- interaction surfaces
- provider and assist workflows

### `uDOS-sonic-screwdriver`

Owns:

- deployment planning
- USB, rescue, and dual-boot bootstrap
- generic install execution and hardware-facing workflows

### `uHOME-server`

Owns:

- home infrastructure runtime
- LAN service model
- household vault examples
- server-side APIs and launcher control
- `uHOME`-specific host-role and bundle contracts

### Downstream client repos

Own:

- Android, TV, and other device-native client implementations

## Ongoing Follow-Through

1. Keep expanding the course and vault scaffolds until they can support concrete
   lessons.
2. Refactor runtime code only when a move sharpens ownership and does not blur
   the repo boundaries.
3. Shrink the deprecated `uhome_server.sonic` namespace until it can be
   removed without affecting repo-local imports.
