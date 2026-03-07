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

## Repository Layout

- `src/uhome_server/` standalone service and install-plan code
- `defaults/workspace/` migrated workspace seed defaults for `uHOME`
- `tests/` focused coverage for migrated routes and Sonic contracts
- `library/` git-backed library manifests and cloned runtime support
- `docs/specs/` implementation-facing specifications
- `docs/decisions/` architecture and product decisions
- `docs/workspace/` migrated workspace templates and instructions

## Development

Install the package and dev dependencies, then run the API with uvicorn:

```bash
python3 -m pip install -e '.[dev]'
python3 -m uvicorn uhome_server.app:app --reload
```

The API exposes:

- `/api/ha/*` for the Home Assistant bridge
- `/api/platform/uhome/*` for presentation status/control
- `/api/library/*` for cloned library repo management
- `/api/containers/*` for manifest-driven container clone/launch status

## License

This project is released under the MIT License. See `LICENSE`.
