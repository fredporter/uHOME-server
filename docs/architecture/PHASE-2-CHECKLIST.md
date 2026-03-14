# Phase 2 Checklist

Status: complete
Updated: 2026-03-09

Phase 2 goal:

- establish `src/uhome_server/installer/` as the active implementation boundary
- reduce `src/uhome_server/sonic/` to compatibility wrappers
- move service-definition ownership earlier into staging so execution and
  promotion consume a staged contract instead of hard-coded service rules
- preserve runtime behavior and test coverage during the boundary cleanup

## Deliverables

- [x] `uhome_server.installer` is the active implementation surface for bundle,
  preflight, plan, staging, execution, promotion, health, and live-apply flows
- [x] `uhome_server.sonic` modules are compatibility wrappers rather than the
  active implementation layer
- [x] compatibility wrappers emit deprecation warnings and repo-local imports
  now target `uhome_server.installer`
- [x] staged installs write a first-class `service-manifest.json`
- [x] execution requires the staged service manifest and copies it into target
  receipts
- [x] promotion and health-check planning consume the staged service manifest
  rather than rebuilding service metadata ad hoc
- [x] CLI and tests use the installer boundary
- [x] full existing test suite remains green

## Deferred Beyond Phase 2

- changing the public bundle schema fields such as `sonic_version`
- removing the legacy `uhome_server.sonic` wrapper layer entirely
