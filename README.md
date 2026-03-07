# uHOME Server

uHOME Server is the standalone local-first home-media and home-operations
server extracted from the `uDOS` home profile lane.

## Migrated Scope

- Home Assistant bridge routes and command handlers
- `uHOME` presentation status/start/stop routes
- file-backed DVR scheduling, playback handoff, and ad-processing settings
- Sonic-side `uHOME` bundle, preflight, and install-plan contracts
- canonical v1.5 `uHOME` specs and decision docs

## Repository Layout

- `src/uhome_server/` standalone service and install-plan code
- `tests/` focused coverage for migrated routes and Sonic contracts
- `docs/specs/` implementation-facing specifications
- `docs/decisions/` architecture and product decisions

## Development

Install the package and dev dependencies, then run the API with uvicorn:

```bash
python3 -m pip install -e '.[dev]'
python3 -m uvicorn uhome_server.app:app --reload
```

The API exposes:

- `/api/ha/*` for the Home Assistant bridge
- `/api/platform/uhome/*` for presentation status/control

## License

This project is released under the MIT License. See `LICENSE`.
