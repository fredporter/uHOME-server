# uHOME Migration Status

Updated: 2026-03-07

This repository now contains the standalone `uHOME` service and documentation
material that was previously stored in the `uDOS` monorepo under explicit
`uHOME`-owned paths.

## Migrated Code

- Home Assistant bridge routes and command handlers
- Home Assistant library/container runtime and standalone gateway service
- `uHOME` presentation service and platform routes
- decentralized node and storage registry routes for multi-server LAN modeling
- dashboard summary and health routes replacing the old Wizard-owned `uHOME`
  summary surface
- Sonic `uHOME` bundle, preflight, and install-plan modules
- focused route/service/install-plan tests
- workspace defaults and instructions for the `uhome` component

## Migrated Docs

- canonical `uHOME` v1.5 spec
- active home-profile decision docs
- kiosk/repo-boundary/Home Assistant bridge decisions
- standalone Sonic release/install guide
- archived `uHOME` roadmap material for hybrid console, LibreELEC, Raspberry Pi,
  and ad-free media lanes
- Home Assistant service docs and dashboard-surface notes formerly kept under
  `uDOS/wizard/`

## Remaining Monorepo Ownership

Any residual `uHOME` references left in `uDOS` should be treated as downstream
consumers, compatibility notes, or historical references rather than the
authoritative home-profile source of truth.
