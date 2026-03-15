# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Health and readiness endpoints (`/api/health`, `/api/ready`, `/api/debug/registries`)
- Backup and restore CLI commands (`uhome backup create`, `uhome backup restore`, `uhome backup list`)
- Shared sync-record contract inspection and envelope validation commands (`uhome contracts ...`)
- Runtime sync-record ingest and retrieval endpoints backed by file-based envelope storage
- Sync-envelope ingest is now reachable from exported `uHOME-empire` sync packages
- Comprehensive operational runbooks (6 guides covering storage, nodes, registries, degradation)
- Deployment Guide for Ubuntu 20.04+ LTS systems
- Post-install validation script for automated deployment verification
- Docker Compose production template with health checks and resource limits
- Observability guide with monitoring, alerting, and capacity planning
- Operations README as central navigation hub for all operational documentation

### Changed
- Improved backup timestamp resolution to include microseconds (prevents filename conflicts)

### Deprecated
- None

### Removed
- None

### Fixed
- None

### Security
- None

## [0.1.0] - 2026-03-10

Initial development release with Phase 5 and Phase 6 (partial) deliverables.

### Added
- FastAPI-based REST server with async request handling
- Household-safe media browsing API with keyword filtering
- Playback status and handoff API for living-room clients
- Launcher capability model and status API
- Node and storage registry system for multi-node deployments
- Library catalog with Jellyfin integration
- Home Assistant bridge service (optional)
- DVR scheduling system (foundation)
- Presentation launcher management (thin-gui, steam-console)
- Installer and preflight system for Ubuntu deployments
- CLI tools: `uhome launcher`, `uhome installer`, `uhome backup`
- 131 comprehensive unit and integration tests
- Development documentation and architecture guides

### Technical Foundation
- Python 3.9+ with type hints and dataclasses
- FastAPI with Pydantic validation
- File-based registries for decentralized node coordination
- Graceful degradation patterns for partial system failures
- Workspace-based configuration system
- Service singleton pattern for shared state

### Documentation
- 6 operational runbooks (storage, nodes, registries, cache, shutdown, degradation)
- Ubuntu 20.04+ deployment guide (11-phase walkthrough)
- Observability guide (monitoring, alerting, capacity planning)
- Release policy documentation (semantic versioning, workflow)
- Phase 1-6 architecture documents and checklists
- Development roadmap and migration status

### Quality Assurance
- 131 passing tests across all modules
- Test coverage for health endpoints, backup/restore, registries, routes, services
- Automated CI validation (tests, linting)
- Post-install validation script for deployment verification

## [0.0.1] - 2026-01-01

Initial project setup (placeholder).

### Added
- Repository structure
- Basic Python package configuration
- Initial CI/CD setup

---

**Note**: This changelog started being maintained consistently from v0.1.0 onwards. Earlier changes may be incomplete.
