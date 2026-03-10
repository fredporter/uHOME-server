# Phase 6 Kickoff: Operational Maturity

Status: active
Started: 2026-03-10
Lead: DevOps / Operations

## Goal

Transition uHOME Server from a development runtime into a maintainable, 
production-grade product with clear operational procedures, deployment automation,
and observability for real-world deployments.

## Context

Phases 1-5 delivered:

- stable REST APIs and client capability model (Phase 5)
- Sonic installer and host profiles for standalone/dual-boot (Phase 4)
- decentralized LAN topology with node and storage registries (Phase 3)
- DVR rule model, job queue, and Jellyfin integration (Phase 2)
- canonical repo structure and documentation (Phase 1)

Phase 6 now shifts focus to operational readiness: making the server deployable,
observable, and recoverable in the wild.

## Deliverables

### Deployment And Configuration

- write deployment guide for Ubuntu 20.04+ LTS hosts
- provide terraform/compose templates for quick stand-up
- document prerequisite checks (Linux kernel, systemd, storage mount points)
- define production config patterns (environment, secrets, persistence)
- provide post-install validation scripts

### Operational Runbooks

- storage degradation recovery (missing volumes, partial availability)
- offline node recovery (secondary server promotion, failover)
- registry recovery (corrupted node/storage registry files)
- library cache invalidation and rebuild
- clean shutdown and state preservation
- graceful degradation patterns

### Release And Versioning

- define semantic versioning for uHOME Server (`major.minor.patch`)
- establish release branch and tag conventions
- create GitHub Releases with release notes and migration guidance
- document breaking change policy and deprecation windows
- package distribution (PyPI, Docker, snap, etc.)

### Backup And Restore

- backup flow for configuration (app settings, workspace settings)
- backup flow for registries (node registry, storage registry, library index)
- backup flow for stateful job queue and DVR schedule
- restore validation and integrity checks
- disaster recovery playbook for complete server loss

### Observability

- structured logging for service startup, API requests, job queue events
- health check endpoints for job queue depth, node connectivity, storage health
- metrics collection points for job execution time, queue wait time
- debug endpoints for inspecting current registries and runtime state
- operator alerting guidance (storage full, jobs stalled, nodes offline)
- dashboard improvements for operator visibility
- alerting rules for critical degradation scenarios

## Current State

### Existing Surfaces

- Service lifecycle managed via systemd (when installed via Sonic)
- Configuration stored in workspace settings files and environment variables
- State persisted in JSON files (registries, library index)
- Job queue exists but has minimal observability
- Node and storage health reported via runtime readiness probes

### Known Gaps

- no single deployment script or terraform templates
- no documented runbooks for common failure modes
- no backup/restore utilities or procedures
- no comprehensive logging or structured observability
- no release engineering workflow or version bumping
- no distribution packaging beyond source install

### Assumptions

- target operator: sys admin or home-lab enthusiast with Linux experience
- target deployment: single-node Ubuntu LTS or small multi-node LAN
- operational window: 24/7 uptime preferred, brief maintenance windows acceptable
- recovery SLA: operator-driven recovery with clear runbooks, not automatic failover

## Success Criteria

- new operators can follow deployment guide to bring up a server in < 30 minutes
- common failure scenarios have documented recovery procedures
- server can be cleanly backed up and restored with state preservation
- releases are reproducible and versioned semantically
- operators can observe job queue health, node connectivity, and storage state
- running server gracefully degrades when nodes or storage disappear

## Out Of Scope For Phase 6

- embedded Kubernetes orchestration (defer to Phase 7+)
- full distributed consensus for node election (defer to Phase 7+)
- high-availability multi-server automatic failover (defer to Phase 7+)
- customer support infrastructure or SLA definitions
- client library SDK releases or packaging (client protocol remains stable from Phase 5)

## Milestones

1. **Baseline Runbooks** (days 1-2)
   - Storage degradation recovery
   - Offline node recovery
   - Registry corruption recovery

2. **Deployment Automation** (days 2-3)
   - Docker compose template for local testing
   - Deployment guide with prerequisite checks
   - Post-install validation script

3. **Backup And Restore** (days 3-4)
   - Backup utility for configs and registries
   - Restore procedure with integrity checks
   - Disaster recovery test

4. **Observability And Logging** (day 4-5)
   - Structured logging for major service components
   - Health check endpoints
   - Operator dashboard or CLI for status inspection

5. **Release Engineering** (day 5)
   - Version bumping and tagging workflow
   - Release notes and changelog
   - Distribution packaging setup

## Technical Approach

### Runbooks

Structure: Assumption → Problem Statement → Detection → Recovery Steps → Validation

Each runbook will document:
- Prerequisites and assumptions
- Symptoms and how to detect the problem
- Step-by-step recovery procedure
- Validation checklist
- Known limitations or gotchas

### Deployment

Provide multiple paths:
- **Quick Start**: Docker compose for local testing
- **Standard Install**: Ubuntu package + systemd, with guided setup
- **Advanced**: Terraform for cloud deployments (AWS, Digital Ocean, etc.)

All paths converge to same configuration model.

### Observability

Implement three tiers:
1. **Operational Health**: Service availability, job queue depth, storage health
2. **Diagnostic**: Request logs, detailed event logs, debug endpoints
3. **Metrics**: Job execution time, queue wait time, API latency

Provide local query tools (CLI) first; leave connection to external monitoring
as optional operator choice.

## Success Measures

Phase 6 complete when:
- All 5 runbooks documented and tested
- Deployment guide + templates exist
- Backup/restore flow is implemented and tested
- Observability endpoints are in place
- Release process is documented
- All Phase 5 tests continue to pass (regression testing)

Exit criteria met when new operator can reproduce:
1. Server deployment from scratch
2. Common failure recovery
3. State backup and restore
4. Health status inspection
