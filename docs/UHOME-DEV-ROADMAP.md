# uHOME Dev Roadmap

Status: active
Updated: 2026-03-10
Lead: AI Roadmap Manager
Scope: standalone `uHOME Server` repository

This roadmap is governed by:

- `docs/uHOME-server-dev-brief.md`
- `docs/uHOME-server-education-dev-brief.md`
- `docs/architecture/UHOME-SERVER-DEV-PLAN.md`

## Goal

Build `uHOME Server` into the canonical Linux-side home-profile runtime:

- standalone Steam-server capable
- Sonic-installable
- LAN-native and local-first
- resilient across multiple potential server nodes
- able to aggregate a household media library from many drives, partitions, and
  cooperating nodes

## Product Shape

### Core server
- Linux-hosted `uHOME Server`
- Jellyfin-backed media serving
- DVR scheduling and post-processing control
- Home Assistant bridge support
- Steam-console and thin-GUI presentation support

### Network topology
- one or more active Linux `uHOME` servers on the LAN
- satellite-style Steam servers for continuity when a stronger dual-boot gaming
  machine is offline
- library availability composed from local and network-visible storage members

### Client surfaces
- Android app
- Google TV app
- Apple TV / tvOS app
- direct-display Linux presentation modes

## Current Baseline

### Already in repo
- Home Assistant bridge routes and gateway scaffold
- `uHOME` presentation service and platform routes
- decentralized node and storage registries
- library/container catalog, clone, and launcher runtime
- Sonic bundle, preflight, and install-plan contracts
- dashboard summary and health routes
- migrated `uHOME` decisions, specs, and service docs

### Current limitations
- storage and node registries now expose topology, authority, recovery, and
  library-availability contracts, but they remain file-backed rather than full
  orchestration
- no authoritative failover or election model yet
- no rich distributed library indexing or replication layer yet
- no packaged production deployment flow yet
- no repo-local frontend client implementation yet

## Phase 1: Runtime Hardening

Goal: make the extracted server reliable as a standalone development runtime.

Deliverables:
- lock dependency versions
- add CI for tests and basic linting
- normalize Python runtime target and local dev bootstrap
- tighten config loading and file-path contracts
- add health and startup checks for Jellyfin and Home Assistant integration

Exit criteria:
- green CI on every push
- repeatable local boot for the server API
- stable container/library manifest handling

## Phase 2: Media And Job Core

Goal: move from scaffolded `uHOME` routes to actual home-media runtime behavior.

Deliverables:
- formal DVR rule model and persistent schedule backend
- job queue for recording, post-processing, and handoff actions
- Jellyfin integration hardening
- media-library path model for local disks and mounted partitions
- structured ad-processing workflow states

Exit criteria:
- DVR rules are durable and queryable
- playback status reflects real Jellyfin state
- background jobs can be queued, observed, and recovered

## Phase 3: Decentralized LAN Model

Goal: turn the multi-server/storage vision into an actual operating model.

Status: complete

Deliverables:
- node capability advertisement and discovery contract
- primary/secondary authority rules for server nodes
- partial-availability model for nodes, drives, and partitions
- aggregated library index across local and peer storage members
- conflict and recovery rules when volumes disappear or reappear

Exit criteria:
- multiple `uHOME` servers can be registered and observed
- storage members can go offline without invalidating the whole library
- active server can report degraded vs healthy topology clearly

## Phase 4: Sonic Install And Host Profiles

Goal: make server deployment first-class for standalone and dual-boot installs.

Status: complete

Deliverables:
- production-ready `uhome-bundle.json` contract examples
- explicit Linux standalone install profile
- explicit Sonic dual-boot disk profile for Linux `uHOME` + Windows 10 gaming
- host capability checks for Steam-server, DVR, and storage roles
- rollback and reinstall validation

Exit criteria:
- Sonic can provision both standalone and dual-boot server lanes
- reinstall/rollback evidence is documented and testable

## Phase 5: Living-Room And Client Integration

Goal: align server APIs and sessions with the real downstream clients.

Status: active (started 2026-03-10)

Deliverables:
- stable server-side contract for Android, Google TV, and Apple TV clients
- launcher/session APIs for remote-first living-room UX
- playback handoff and target selection semantics
- household-safe browsing/status endpoints
- client capability model for controller, remote, and touch surfaces

Exit criteria:
- client apps can consume a stable server contract
- server can target multiple living-room surfaces cleanly

## Phase 6: Operational Maturity

Status: core Phase 6 checklist complete (started 2026-03-10, Session 2 completed 2026-03-10, tranche follow-up 2026-03-22)

Goal: make `uHOME Server` maintainable as its own public product.

Deliverables:
- ✅ deployment guide for Ubuntu-class hosts (11-phase guide + post-install validation)
- ✅ operational runbooks for degraded storage and offline nodes (6 comprehensive runbooks)
- ✅ release process and versioning policy (RELEASE-POLICY.md + CHANGELOG.md)
- ✅ backup/restore flow for config, registry, and library metadata (CLI + 13 tests)
- ✅ observability for job queue, node health, and storage health (health endpoints + guide)
- ✅ environment configuration guide and checked-in env example
- ✅ prerequisite checker for kernel, systemd, workspace, and storage paths

Exit criteria:
- ✅ public releases are reproducible (tagging workflow documented)
- ✅ operator recovery steps are documented (6 runbooks with scenarios)
- ✅ server state can be backed up and restored cleanly (uhome backup CLI)
- ✅ health endpoints available for monitoring (3 endpoints: health, ready, debug)
- ✅ all tests passing (196 tests, zero regressions)

Deferred to future:
- PyPI/Docker Hub publishing automation (manual process documented)
- Terraform cloud deployment templates (optional)

## Cross-Cutting Priorities

- keep Linux as the authoritative server runtime
- treat Windows gaming as auxiliary in dual-boot installs
- preserve local-first behavior
- degrade gracefully when nodes or storage disappear
- keep client apps downstream of server contracts rather than embedding them in
  this repo

##~~add dependency lockfiles~~ ✓ completed 2026-03-10
- ~~add Jellyfin integration tests and configuration docs~~ ✓ completed 2026-03-10
- extract playback routes from Home Assistant command-handler scaffolding
- broaden node authority states and transitions beyond current primary handoff
- define storage volume identity rules beyond mount path current primary handoff
- define storage volume identity rules beyond mount paths
- add Jellyfin integration tests and configuration docs
- define API contract for downstream TV/mobile clients
