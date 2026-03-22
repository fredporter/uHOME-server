# Triage: uHOME v2 Master Architecture Specification

- title: uHOME v2 Master Architecture Specification
- date: 2026-03-15
- related binder: `#binder/uhome-v2-architecture-alignment`
- related repos:
  - `uDOS-dev`
  - `uHOME-server`
  - `uHOME-client`
  - `uHOME-empire`
- status: `triaged`

## Summary

This brief is a cross-repo architecture recommendation for the `uHOME` family.
It expands the current server, client, and empire framing into a fuller
household platform with Matter and platform-specific kiosk clients.

## Findings

- the direction is compatible with the current family boundary model
- `uHOME-server` and `uHOME-empire` already align with major parts of the brief
- `uHOME-client` currently carries the shared runtime role that the brief wants
  to project through the active Android and iOS app repos
- `uHOME-app-android` and `uHOME-app-ios` are now the active v2 mobile app
  repos
- `uHOME-matter` is already active as the automation extension lane, so the
  main remaining work is documentation and platform-app depth rather than repo activation

## Risks

- updating family docs as if the new repos already exist would make governance
  drift from the actual workspace
- replacing `uHOME-client` prematurely would erase the current runnable client
  lane without a concrete successor
- treating Matter as already separated could create false repo-boundary claims

## Next Actions

- adopt the architecture direction as a staged recommendation
- update `uDOS-dev` docs to distinguish active repos from planned split targets
- route the brief into a canonical `uDOS-dev` alignment note
- open a dedicated binder for the eventual repo-split work
