# Phase 5 Checklist

Status: complete
Started: 2026-03-10
Updated: 2026-03-10
Completed: 2026-03-10

## Goal

Establish stable server-side contracts for downstream Android, Google TV, and
Apple TV clients and align runtime behavior with remote client expectations.

## Deliverables

### API Contract Stability

- [x] document stable REST API surfaces for client consumption
- [x] consolidate launcher, session, and playback handoff into first-class
      routes
- [x] define household-safe browsing and status endpoints
- [x] establish client capability model (controller, remote, touch)

### Runtime Refactoring

- [x] extract playback status and handoff from Home Assistant command-handler
      scaffolding
- [x] promote `playback_status` and `playback_handoff` to REST API routes under
      `/api/playback/*`
- [x] align launcher and session concepts with downstream client needs
- [x] separate media status from runtime readiness probes

### Documentation

- [x] write API contract examples for Android, Google TV, and Apple TV clients
- [x] document client authentication and discovery patterns
- [x] add examples for playback handoff, launcher session, and media browsing
- [x] document client-side capability advertisement contracts

### Testing

- [x] add tests for new `/api/playback/*` routes
- [x] validate launcher and session handoff from client perspective
- [x] ensure household-safe endpoint behavior is tested

## Exit Criteria

- [x] stable REST API contract is documented and versioned
- [x] client apps can consume the contract without tight server coupling
- [x] launcher, session handoff, and playback control are first-class REST
      operations
- [x] household browsing and status endpoints are safe for living-room UX
- [x] full current test suite remains green

## Progress Summary

**Completed (2026-03-10):**

✅ **Playback API** - First-class REST API for media playback control
  - Routes: `/api/playback/status`, `/api/playback/handoff`, `/api/playback/queue`
  - Service: `PlaybackService` extracted from Home Assistant scaffolding
  - Tests: 9 new tests for playback routes, 8 Jellyfin integration tests
  - Documentation: `docs/clients/PLAYBACK-API.md` with platform examples

✅ **Launcher API** - First-class REST API for session management
  - Routes: `/api/launcher/status`, `/api/launcher/start`, `/api/launcher/stop`
  - Service: Uses existing `UHomePresentationService` with clean REST interface
  - Tests: 8 new tests for launcher routes
  - Documentation: `docs/clients/LAUNCHER-API.md` with platform examples

✅ **Household API** - Living-room-safe browsing and runtime status
  - Routes: `/api/household/status`, `/api/household/browse`
  - Service: `HouseholdService` with keyword-based safety filtering
  - Tests: 4 new household route tests for filtering and status behavior
  - Documentation: `docs/clients/HOUSEHOLD-API.md` contract reference

✅ **Client Capability Model** - Defined capability profiles
  - Profiles: controller, remote, touch
  - Documentation: `docs/clients/CLIENT-CAPABILITIES.md`
  - Platform detection examples for Android, iOS/tvOS, JavaScript

✅ **Client Integration Guide** - Comprehensive getting-started guide
  - Documentation: `docs/clients/INTEGRATION-GUIDE.md`
  - Platform-specific guidelines for Android, Google TV, Apple TV, iOS, web
  - Discovery, authentication, error handling, testing examples

✅ **Test Suite** - 106 tests passing
  - 77 original tests (Phases 1-4)
  - +8 Jellyfin integration tests
  - +9 playback route tests
  - +8 launcher route tests
  - +4 household route tests

## Deferred Beyond Phase 5

- embedding client implementations in this repo
- advanced household-role or profile models
- production packaging or release engineering for clients (Phase 6)
