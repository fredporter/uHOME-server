# Phase 3 LAN Kickoff

Status: complete
Updated: 2026-03-09

Phase 3 starts the decentralized LAN operating-model work inside
`uHOME-server`.

## Goal

Turn the existing file-backed node and storage registries into a clearer LAN
contract that can report household topology health without pretending full
orchestration already exists.

## First Move

Introduce a repo-local topology summary contract that:

- validates node authority and node or volume status values
- distinguishes healthy, degraded, and offline topology states
- reports active primary nodes and partial-availability issues
- exposes the summary through the existing network API surface

Current progress:

- topology summary is live at `/api/network/topology`
- primary authority handoff now promotes exactly one active primary
- demoting the last active primary is rejected until a replacement is promoted

## Why This Slice Comes First

- it advances the actual operating model for multi-node `uHOME` deployments
- it keeps the work inside the current file-backed registry boundary
- it gives later Phase 3 work a stable contract for authority rules and
  degraded-topology reporting

## Next Targets

1. define storage identity beyond raw mount paths
2. move from registry-advertised library membership toward richer distributed
   library indexing
3. formalize richer recovery rules when nodes disappear and later return
