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
