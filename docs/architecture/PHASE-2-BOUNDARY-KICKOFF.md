# Phase 2 Boundary Kickoff

Status: complete
Updated: 2026-03-08

Phase 2 starts the runtime-boundary cleanup after the Phase 1 information
architecture work.

## First Move

Introduce `src/uhome_server/installer/` as the neutral public import surface
for:

- bundle contracts
- preflight
- install planning
- staging and execution
- promotion and verification
- host health checks
- guarded live apply

Phase 2 outcome:

- `src/uhome_server/installer/` is now the active implementation boundary
- `src/uhome_server/sonic/` is now the deprecated legacy compatibility layer
- staged service manifests now drive execution and promotion flows

That staging-to-promotion cleanup is complete: the staged service manifest now
drives execution and promotion so generic host-apply steps no longer depend on
hard-coded `uHOME` service lookup rules.

## Why This Phase Is Complete

- it sharpens the public ownership boundary without moving runtime code yet
- it preserves the current package and tests
- it gives future `uHOME-server` work a stable place to land without spreading
  installer ownership across unrelated package surfaces

See `docs/architecture/PHASE-2-CHECKLIST.md` for the deliverable list.

## Next Targets

1. keep only `uHOME`-specific host-role, bundle, and server-contract logic in
   `uHOME-server`
2. remove the deprecated `uhome_server.sonic` wrapper layer when compatibility
   is no longer required
