# Phase 5 Kickoff: Living-Room And Client Integration

Status: complete
Started: 2026-03-10
Completed: 2026-03-10

## Goal

Establish stable server-side contracts for downstream client implementations
and align the runtime behavior with remote client expectations.

## Context

Phases 1-4 delivered:

- standalone installer and deployment infrastructure (Phase 4)
- decentralized node and storage topology (Phase 3)
- clear installer boundary and service manifests (Phase 2)
- canonical repo structure and documentation (Phase 1)

Phase 5 now shifts focus to the client-facing experience and API stability for
living-room surfaces.

## Deliverables

### Server-Side Contract Stability

- document stable API surfaces for downstream Android, Google TV, and Apple TV
  clients
- consolidate launcher, session, and playback handoff semantics into explicit
  client contracts
- define household-safe browsing and status endpoints
- establish client capability model for controller, remote, and touch surfaces

### Runtime Alignment

- separate media status, session targeting, and playback control from broader
  command-handler scaffolding
- promote `playback_status` and `playback_handoff` to first-class REST API
  routes
- align server-side session and launcher concepts with downstream client needs

### Documentation And Examples

- write API contract examples for each expected client lane
- document client authentication and discovery patterns
- add examples for playback handoff, launcher session, and media browsing flows

## Current State

### Existing Surfaces

- `/api/platform/uhome/*` provides launcher status and control
- `/api/containers/*` provides library catalog and clone operations
- playback handoff exists in Home Assistant command handlers but is not yet a
  first-class REST route
- Jellyfin-backed media status is reported through runtime readiness probes

### Known Gaps

- playback and session APIs are still coupled to Home Assistant bridge logic
- no explicit client authentication or session-token model
- no documented contract for remote client discovery or registration
- no client-side capability advertisement (controller vs remote vs touch)

## Success Criteria

- stable REST API contract for clients can be documented and versioned
- client apps can consume the contract without tight coupling to server
  implementation details
- server routes support launcher, session handoff, and playback control as
  first-class operations
- household browsing and status endpoints are safe for living-room UX

## Out Of Scope For Phase 5

- embedding client implementations in this repo
- advanced profile or household-role models beyond basic server targeting
- production packaging or release engineering for clients (Phase 6 concern)
