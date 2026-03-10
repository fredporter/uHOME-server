# Roadmap Status Update

Status: active
Updated: 2026-03-10
Lead: AI Roadmap Manager

## Summary

The uHOME Server roadmap has been taken over with active development focus on
Phase 5 (Living-Room And Client Integration) and Phase 6 (Operational Maturity)
planning.

## Completed Today

### Infrastructure Improvements

- **Dependency Lockfiles**: Added `requirements.lock` for reproducible builds
  and CI stability
- **CI Enhancement**: Updated GitHub Actions workflow to use lockfile
- **Documentation**: Created dependency management guide at
  `docs/howto/DEPENDENCY-MANAGEMENT.md`

### Phase 5 Planning

- **Phase 5 Kickoff**: Documented client integration goals and deliverables
- **Phase 5 Checklist**: Created detailed checklist for living-room client work
- **API Contract**: Identified current surfaces and gaps for downstream clients

### Phase 6 Planning

- **Phase 6 Kickoff**: Documented operational maturity goals
- **Phase 6 Checklist**: Created detailed checklist for deployment and release
  engineering

### Jellyfin Integration

- **Documentation**: Created comprehensive Jellyfin integration guide at
  `docs/howto/JELLYFIN-INTEGRATION.md`
- **Testing**: Added 8 new integration tests covering:
  - Configuration and reachability
  - Unconfigured state handling
  - Connection failures and timeouts
  - Invalid API key handling
  - Malformed response handling
  - Runtime readiness probe integration

## Test Status

- **Total Tests**: 85 (was 77)
- **Status**: All passing
- **New Coverage**: Jellyfin integration scenarios

## Phase Status

- **Phase 1**: Complete (Information Architecture)
- **Phase 2**: Complete (Installer Boundary)
- **Phase 3**: Complete (Decentralized LAN Model)
- **Phase 4**: Complete (Sonic Install And Host Profiles)
- **Phase 5**: Planned and documented (Living-Room And Client Integration)
- **Phase 6**: Planned and documented (Operational Maturity)

## Near-Term Priorities

### Immediate (Next Session)

1. Begin Phase 5 implementation:
   - Extract playback routes from Home Assistant scaffolding
   - Create first-class `/api/playback/*` endpoints
   - Document stable client API contract

2. Continue infrastructure work:
   - Enhance node authority state transitions
   - Define storage volume identity contracts

### Short-Term (This Week)

3. Phase 5 API work:
   - Consolidate launcher and session semantics
   - Add client capability model
   - Write API contract examples

4. Documentation:
   - Add deployment guide for Ubuntu hosts
   - Document backup/restore flows

### Medium-Term (This Month)

5. Complete Phase 5:
   - Client authentication patterns
   - Living-room UX endpoints
   - Household-safe browsing

6. Begin Phase 6:
   - Release automation
   - Operational runbooks
   - Observability improvements

## Repository Health

- **CI**: Green on all pushes
- **Dependencies**: Locked and reproducible
- **Test Coverage**: 85 tests, all passing
- **Documentation**: Phase kickoff docs in place

## Decisions Made

- Adopted `requirements.lock` for reproducible builds over poetry/pipenv
- Phase 5 focuses on server-side contract stability, not embedding client apps
- Phase 6 defers cloud/SaaS deployments in favor of Ubuntu-class host maturity

## Next Actions

1. Mark Phase 5 as active in roadmap
2. Begin playback route extraction work
3. Define client API versioning strategy
4. Continue node authority enhancement work

## Files Changed

- Created: `requirements.lock`
- Created: `docs/howto/DEPENDENCY-MANAGEMENT.md`
- Created: `docs/howto/JELLYFIN-INTEGRATION.md`
- Created: `docs/architecture/PHASE-5-KICKOFF.md`
- Created: `docs/architecture/PHASE-5-CHECKLIST.md`
- Created: `docs/architecture/PHASE-6-KICKOFF.md`
- Created: `docs/architecture/PHASE-6-CHECKLIST.md`
- Created: `tests/test_jellyfin_integration.py`
- Modified: `.github/workflows/ci.yml`
