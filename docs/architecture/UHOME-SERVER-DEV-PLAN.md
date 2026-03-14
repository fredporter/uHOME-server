# uHOME Server Dev Plan

Status: active
Updated: 2026-03-09
Scope: repo-local development plan for `uHOME-server`

## Governing Inputs

This plan is derived from two local briefs and the active repo roadmap:

- `docs/uHOME-server-dev-brief.md`
- `docs/uHOME-server-education-dev-brief.md`
- `docs/UHOME-DEV-ROADMAP.md`

The briefs are not background reading only. They define the development model
and the target repo shape for `uHOME-server`.

## What Each Brief Controls

### `docs/uHOME-server-dev-brief.md`

Sets the repo's development workflow expectations:

- align `uHOME-server` with the `@dev` workspace and binder model used by
  `uDOS`
- keep local development scaffolding separate from the curated distributable
  repo
- organize work around milestones, objectives, review, compile, and promotion

### `docs/uHOME-server-education-dev-brief.md`

Sets the repo's education-facing structure expectations:

- treat `uHOME-server` as the home-infrastructure pathway in the `uDOS` family
- use the shared root language: `apps/`, `modules/`, `services/`, `vault/`,
  `docs/`, `courses/`, `scripts/`, `config/`, and `tests/`
- teach local-network service building through vault examples, modules,
  services, and course scaffolds

### `docs/UHOME-DEV-ROADMAP.md`

Turns those two briefs into phased delivery work for the live repo.

## Current Plan

### Phase 1: Information Architecture

Status: complete

Anchor docs:

- `docs/architecture/PHASE-1-CHECKLIST.md`
- `docs/architecture/PHASE-1-IA-MAP.md`

Outcome:

- the repo now exposes the education-facing top-level structure without moving
  the live runtime package

### Phase 2: Installer Boundary Cleanup

Status: complete

Anchor docs:

- `docs/architecture/PHASE-2-CHECKLIST.md`
- `docs/architecture/PHASE-2-BOUNDARY-KICKOFF.md`

Outcome:

- `uhome_server.installer` is the active repo-local installer surface
- `uhome_server.sonic` is deprecated compatibility-only

### Phase 3: Decentralized LAN Model

Status: complete

Anchor docs:

- `docs/architecture/PHASE-3-LAN-KICKOFF.md`
- `docs/architecture/PHASE-3-CHECKLIST.md`

Outcome:

- topology, primary authority, partial availability, and aggregated
  library-availability contracts are now explicit in the repo-local network
  surface

### Phase 4: Install And Host Profiles

Status: complete

Anchor docs:

- `docs/architecture/PHASE-4-HOST-PROFILES-KICKOFF.md`
- `docs/architecture/PHASE-4-CHECKLIST.md`
- `docs/architecture/PHASE-4-COMPLETION.md`

Outcome:

- standalone and dual-boot example lanes now act as canonical host-profile
  references for the installer surface

### Phase 5+: Runtime And Product Work

Status: active backlog

Anchor doc:

- `docs/UHOME-DEV-ROADMAP.md`

This is the active delivery track after the repo-structure work:

1. Media and job core
2. Living-room and client integration
3. Operational maturity

## Working Rules

- build work in this repo must stay consistent with both local briefs
- repo-local implementation work should land against the phased roadmap, not as
  isolated one-off refactors
- new documentation and structural work should reinforce the education-facing
  root model
- new runtime work should use `uhome_server.installer`, not the deprecated
  `uhome_server.sonic` namespace

## Start Here

If you are planning or advancing work in `uHOME-server`, read in this order:

1. `docs/architecture/UHOME-SERVER-DEV-PLAN.md`
2. `docs/uHOME-server-dev-brief.md`
3. `docs/uHOME-server-education-dev-brief.md`
4. `docs/UHOME-DEV-ROADMAP.md`
