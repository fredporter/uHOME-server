# Phase 4 Host Profiles Kickoff

Status: complete
Updated: 2026-03-09

Phase 4 starts the install-profile and deployment-contract work inside
`uHOME-server`.

## Goal

Make standalone and dual-boot deployment lanes explicit in the repo-local
installer surface so example bundles, preflight checks, and generated install
plans all agree on the intended host shape.

## First Move

Introduce named host profiles into the bundle and preflight contract:

- bundle manifests declare a `host_profile`
- preflight can resolve named standalone and dual-boot profiles
- example bundles and probes validate against those explicit profiles
- generated install plans carry the resolved host profile forward

Current progress:

- named host profiles now flow through bundle, preflight, and plan generation
- role-specific capability checks now cover media, DVR, launcher, Steam, and
  dual-boot expectations
- staged and promoted receipts now carry host-profile, rollback, and reinstall
  evidence

## Why This Slice Comes First

- it turns the existing example bundles into actual deployment-profile
  contracts rather than generic installer samples
- it sharpens the difference between standalone Linux hosts and dual-boot Steam
  nodes without changing repo ownership boundaries
- it gives later Phase 4 work a stable place to hang richer host capability,
  rollback, and reinstall evidence

## Next Targets

1. move from host-profile contracts into broader deployment and release
   operations
2. deepen disk and storage identity handling beyond the current evidence model
3. keep generic deployment ownership out of `uHOME-server`
