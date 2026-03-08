# Phase 3 Checklist

Status: complete
Updated: 2026-03-09

Phase 3 goal:

- establish a clearer decentralized LAN operating model inside `uHOME-server`
- make node authority, partial availability, and topology health explicit
- aggregate library availability across local and peer storage members
- preserve the current file-backed registry boundary while hardening the
  contracts

## Deliverables

- [x] node authority and node or volume status values are validated
- [x] topology health reports `healthy`, `degraded`, or `offline`
- [x] active primary authority is enforced through explicit handoff rules
- [x] demoting the last active primary is rejected until a replacement exists
- [x] storage recovery transitions distinguish steady, missing, and returned
- [x] aggregated library availability is reported across local and peer volumes
- [x] offline or missing volumes degrade library availability without
  invalidating the whole library surface
- [x] network API exposes topology and aggregated library-index contracts
- [x] dashboard network summary reports topology status and library-index health
- [x] full test suite remains green

## Delivered Surfaces

- `src/uhome_server/cluster/registry.py`
- `src/uhome_server/routes/network.py`
- `src/uhome_server/routes/dashboard.py`
- `tests/test_network_registry.py`
- `tests/test_dashboard_routes.py`

## Deferred Beyond Phase 3

- durable storage identity contracts beyond current volume records and metadata
- distributed library indexing beyond registry-advertised volume membership
- automatic failover or election between `uHOME` server nodes
