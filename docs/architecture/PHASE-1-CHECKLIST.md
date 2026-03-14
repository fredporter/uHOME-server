# Phase 1 Checklist

Status: complete
Updated: 2026-03-08

Phase 1 goal:

- define the public entrypoints for Use / Learn / Build
- decide which existing roots are canonical, redirected, or transitional
- document the first stable `apps/`, `modules/`, `services/`, and `vault/`
  teaching language without renaming runtime roots yet
- document the companion-repo family model so cross-repo work stays legible

## Deliverables

- [x] public `Use / Learn / Build` entrypoints exist in the root README and
  pathway docs
- [x] canonical `apps/`, `modules/`, `services/`, `vault/`, `courses/`,
  `config/`, and `scripts/` roots exist with README coverage
- [x] root classification policy exists for canonical and transitional surfaces
- [x] current-to-target mapping exists for the live runtime package
- [x] repo family model exists for `uDOS-core`, `uDOS-shell`, `uDOS-wizard`,
  `uHOME-server`, `uDOS-sonic-screwdriver`, and downstream clients
- [x] no-break policy is documented and keeps `src/uhome_server/` as the active
  implementation package

## Deferred To Later Phases

- runtime code relocation out of `src/uhome_server/`
- deeper narrowing of `src/uhome_server/sonic/`
- vault-backed runtime replacement for current file-backed state
- full lesson structure with checkpoints, exercises, and projects
