# uHOME Brief Implementation Checklist

- date: 2026-03-16
- tag: @dev/uhome-brief-implementation-pass
- scope:
  - @dev/inbox/briefs/uhome_v_2_master_spec.md
  - @dev/inbox/briefs/uhome_v_2_empire.md
  - linkage check against uHOME-server, uHOME-empire, uDOS-wizard, sonic-screwdriver

## Repo Checklist

| repo | implemented | partial | next action |
| --- | --- | --- | --- |
| uHOME-server | Runtime sync and automation loop is live (`/api/runtime/sync-records/*`, `/api/runtime/automation/*`). Launcher, playback, household, dashboard, and network topology APIs are present. Jellyfin status and handoff pathways are wired into runtime probes and playback status. | Roadmap still lists missing authoritative failover/election and richer distributed indexing/replication. Advanced networking profile semantics from the brief (Beacon/Crypt/Tomb policy ownership handshake) are not yet represented as explicit server-owned contracts. Client capability registration is documented but not yet exposed as a server route. | 1) add a failover/election contract and node-authority state machine tests. 2) add client capability registration and state endpoints aligned to docs/clients/CLIENT-CAPABILITIES.md. 3) define server-side policy ingestion contract for Wizard-managed networking profiles. |
| uHOME-empire | Operations-container spine is active (`packs/`, `schemas/pack-manifest.schema.json`, `src/sync_adapter.py`, smoke scripts). Starter packs support `approval_mode`, `dry_run_supported`, template rendering, and runtime handoff summary. Sync-package and automation-job/result handoff into uHOME-server routes is implemented, including local in-process probes. | Provider lanes are intentionally scaffolded, not fully live provider runtimes. Phase 2 to Phase 4 roadmap items remain open: audience segmentation depth, stronger approval workflow conventions, editable pack builders, and extended adapters (WordPress/headless/community distribution). | 1) promote one provider lane (HubSpot or Google) from scaffolded to active with explicit failure policy and runbook. 2) implement first audience-segmentation and approval-gate runtime primitives. 3) add one extended publishing adapter (WordPress/headless) with tests and smoke flow. |
| uDOS-wizard | Orchestration contract is published (`contracts/orchestration-contract.json`) with status, dispatch, workflow-plan, callback, and result routes. Wizard has uHOME bridge endpoints and runtime automation relay routes that target uHOME-server automation APIs. | uHOME networking profile policy package for Beacon/Crypt/Tomb/Home is not yet pinned as a concrete cross-repo contract artifact consumed by uHOME-server. | 1) publish a versioned Wizard-to-uHOME networking policy contract artifact and schema. 2) add end-to-end tests that validate policy handoff and server acceptance behavior. |
| sonic-screwdriver | Boundary is clear that uHOME runtime bundle/preflight/install-plan source of truth is uHOME-server. First-run preflight, Linux quickstart, and structure checks are in place for deployment lane validation. | No direct ownership of uHOME runtime semantics by design. Cross-repo contract conformance checks against current uHOME-server install/bundle contract versions are not yet surfaced as an explicit Sonic smoke artifact. | 1) add a cross-repo conformance smoke that checks Sonic deployment assumptions against uHOME-server contract versions. 2) keep Sonic docs pinned to uHOME-server as contract source of truth for install/bundle/preflight surfaces. |

## Link Map

- uHOME-empire -> uDOS-wizard
  - uses Wizard orchestration contract (`uDOS-wizard/contracts/orchestration-contract.json`) for transport target attachment and probe flow
- uHOME-empire -> uHOME-server
  - dispatches to server ingest and automation routes (`/api/runtime/sync-records/ingest`, `/api/runtime/automation/jobs`, `/api/runtime/automation/process-next`, `/api/runtime/automation/results`)
- uDOS-wizard -> uHOME-server
  - bridge routes proxy runtime automation status, queue, processing, retry, cancel, and reconciliation
- sonic-screwdriver -> uHOME-server
  - deployment repo consumes uHOME contract outputs but does not own runtime behavior

## Suggested Binder Follow-Up

- binder: #binder/uhome-v2-implementation-gap-pass
- owner: uDOS-dev
- objective:
  - convert this checklist into repo-specific requests for uHOME-server, uHOME-empire, uDOS-wizard, and sonic-screwdriver
- promotion path:
  - triage -> requests -> submissions
