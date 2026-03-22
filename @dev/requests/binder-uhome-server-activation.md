# Request: `#binder/uhome-server-activation`

- title: Activate `uHOME-server` as the next Tranche 4 repo-facing implementation surface
- requested by: v2 roadmap workflow
- owning repo or stream: `uHOME-server`
- binder: `#binder/uhome-server-activation`
- summary: Add the first repo-level activation and validation flow for `uHOME-server` while keeping server ownership inside persistent local services, scheduling, and server-owned runtime checks.
- acceptance criteria:
  - `uHOME-server` exposes an activation doc
  - `uHOME-server` exposes a local validation command under `scripts/`
  - `uHOME-server` includes a minimal operator walkthrough
  - repo entry surfaces point to the activation flow
- dependencies:
  - `#binder/core-contract-enforcement`
  - `#binder/wizard-activation`
  - `uHOME-server` current FastAPI and CLI package surfaces under `src/uhome_server/`
- boundary questions:
  - activation should stay inside server-owned service and scheduling surfaces
  - shell UX remains in `uDOS-shell`
  - provider-backed assistance remains in `uDOS-wizard`
- due or milestone: v2 roadmap tranche 4

## Binder Fields

- state: `completed`
- owner: `uHOME-server`
- dependent repos:
  - `uDOS-dev`
- blocked by:
  - none
- target branch: `develop`
- objective:
  - make `uHOME-server` runnable and teachable without broadening its ownership boundary
- promotion criteria:
  - server activation docs, example, and validation entrypoint are committed
  - roadmap ledger reflects `uHOME-server` as the active repo-activation binder
- files or areas touched:
  - `uHOME-server/docs`
  - `uHOME-server/scripts`
  - `uHOME-server/examples`
  - `uDOS-dev/@dev`

## Lifecycle Checklist

- [x] Open
- [x] Hand off
- [x] Advance
- [x] Review
- [x] Commit
- [x] Complete
- [x] Compile
- [x] Promote
