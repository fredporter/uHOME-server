# Phase 4 Completion

Status: complete
Updated: 2026-03-09

Phase 4 established explicit install and host-profile lanes for
`uHOME-server`.

## What Is Now Canonical

- example bundles under `examples/installer/bundles/standalone/` and
  `examples/installer/bundles/dual-boot/`
- example probes under `examples/installer/probes/`
- host-profile-aware installer surfaces in `src/uhome_server/installer/`
- operator guidance in `docs/howto/UHOME-INSTALL-LANES.md`

## Delivered Contract

- bundle manifests declare the intended host profile
- preflight resolves standalone and dual-boot lanes explicitly
- staged receipts carry host-profile, rollback, and storage-identity evidence
- promoted receipts carry reinstall context
- verification checks assert host-profile, rollback, and storage-identity
  evidence
- example flows are covered by tests rather than left as documentation-only

## What Phase 4 Does Not Claim

- generic deployment ownership beyond `uHOME`-specific host profiles
- full disk orchestration or partition management
- release engineering or public packaging maturity

Those remain later-phase work.
