# Build on uHOME Server

Use this path if you want to extend the runtime, advance the refactor, or work
on the cross-repo family model.

## Start With

1. `docs/architecture/UHOME-SERVER-DEV-PLAN.md`
2. `docs/uHOME-server-dev-brief.md`
3. `docs/uHOME-server-education-dev-brief.md`
4. `docs/architecture/PHASE-1-IA-MAP.md`
5. `docs/architecture/ROOT-POLICY.md`
6. `docs/pathway/REPO-FAMILY.md`
7. `docs/architecture/PHASE-3-LAN-KICKOFF.md`
8. `docs/architecture/PHASE-3-CHECKLIST.md`
9. `docs/architecture/PHASE-4-HOST-PROFILES-KICKOFF.md`
10. `docs/architecture/PHASE-4-CHECKLIST.md`
11. `docs/howto/UHOME-INSTALL-LANES.md`
12. `src/uhome_server/`

## Active Build Rules

- treat the two local briefs as governing inputs to the dev plan
- keep the runtime package under `src/uhome_server/` until a move sharpens
  ownership
- prefer the new top-level roots for teaching language and repo entrypoints
- keep `uHOME` runtime ownership separate from generic deployment ownership
- keep client implementations downstream of server contracts

## Good Next Targets

- remove remaining repo-local references to the deprecated
  `uhome_server.sonic` namespace
- keep growing vault-backed examples
- replace placeholder file-backed scheduling behavior with a durable backend
- broaden storage identity and recovery rules beyond the current file-backed LAN
  contract
