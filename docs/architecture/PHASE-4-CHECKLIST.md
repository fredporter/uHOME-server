# Phase 4 Checklist

Status: complete
Updated: 2026-03-09

Phase 4 goal:

- make standalone and dual-boot deployment lanes explicit in `uHOME-server`
- turn installer examples into profile-aware deployment contracts
- carry host-profile, rollback, and reinstall evidence through the installer
  flow
- prepare the repo for a bounded Phase 4 closeout

## Delivered So Far

- [x] bundle manifests declare named `host_profile` contracts
- [x] preflight resolves standalone and dual-boot host profiles
- [x] generated install plans carry the resolved host profile forward
- [x] example bundles and probes validate against explicit host profiles
- [x] role-specific capability checks cover media, DVR, launcher, Steam, and
  dual-boot expectations
- [x] staged receipts include host-profile and rollback evidence
- [x] promoted receipts include reinstall context
- [x] promoted-host verification checks for host-profile and rollback evidence
- [x] the installer CLI can run preflight against named host profiles
- [x] full current test suite remains green

## Closeout Tasks

- [x] document standalone and dual-boot install lanes as explicit operator flows
- [x] add stronger disk-layout or storage-identity evidence for host profiles
- [x] validate rollback and reinstall behavior against the example lanes more
  explicitly than current receipt assertions
- [x] write a Phase 4 completion note that ties the examples, installer
  surfaces, and docs together

## Exit Criteria

- standalone and dual-boot install lanes are documented and testable
- reinstall and rollback evidence is both documented and verified in tests
- host-profile-aware examples can be used as the canonical Phase 4 references
- remaining deployment work is clearly deferred beyond Phase 4 rather than left
  ambiguous
