# Docs

`docs/` is the reference-first documentation root for `uHOME-server`.

Tutorial and student-facing step-through material belongs in `courses/`. This
root is for architecture, pathway, client, operational, and implementation
documentation tied to the real repo.

## Entry Points

### Use

- [USE.md](pathway/USE.md) for the current operator path
- [UHOME-DASHBOARD.md](ui/UHOME-DASHBOARD.md) for the dashboard surface
- [SONIC-STANDALONE-RELEASE-AND-INSTALL.md](howto/SONIC-STANDALONE-RELEASE-AND-INSTALL.md)
  for release and install guidance

### Learn

- [README.md](pathway/README.md) in `docs/pathway/` for repo positioning
- [uHOME-server-education-dev-brief.md](uHOME-server-education-dev-brief.md)
  for the local pathway brief
- [UHOME-v1.5.md](specs/UHOME-v1.5.md) for the current canonical spec

### Build

- [UHOME-SERVER-DEV-PLAN.md](architecture/UHOME-SERVER-DEV-PLAN.md) for the
  active repo-local development plan
- [uHOME-server-dev-brief.md](uHOME-server-dev-brief.md) for the repo workflow
  and binder-alignment brief
- [uHOME-server-education-dev-brief.md](uHOME-server-education-dev-brief.md)
  for the education-structure brief
- [PHASE-1-IA-MAP.md](architecture/PHASE-1-IA-MAP.md) for current-to-target mapping
- [ROOT-POLICY.md](architecture/ROOT-POLICY.md) for canonical vs transitional roots
- [PHASE-1-CHECKLIST.md](architecture/PHASE-1-CHECKLIST.md) for the completed
  Information Architecture deliverables
- [PHASE-2-CHECKLIST.md](architecture/PHASE-2-CHECKLIST.md) for the completed
  installer-boundary cleanup inside `uHOME-server`
- [PHASE-3-CHECKLIST.md](architecture/PHASE-3-CHECKLIST.md) for the completed
  decentralized LAN-model milestone
- [PHASE-3-LAN-KICKOFF.md](architecture/PHASE-3-LAN-KICKOFF.md) for the
  kickoff and boundary notes for the LAN-model phase
- [REPO-FAMILY.md](pathway/REPO-FAMILY.md) for family-boundary and companion-repo rules
- the deprecated `uhome_server.sonic` namespace is compatibility-only; new
  repo-local work should use `uhome_server.installer`

## Sections

- `architecture/` for repo-shape and migration policy
- `clients/` for downstream client-contract positioning
- `courses/` for maintainer notes about the learning path
- `decisions/` for architectural and product decisions
- `howto/` for operational runbooks
- `pathway/` for cross-repo positioning and entrypoint docs
- `services/` for service-level operational docs
- `specs/` for implementation-facing specifications
- `ui/` for dashboard and client-surface contracts
- `workspace/` for workspace templates and instructions
