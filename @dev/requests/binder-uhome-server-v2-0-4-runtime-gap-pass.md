# Request: `#binder/uhome-server-v2-0-4-runtime-gap-pass`

- title: Close the remaining `uHOME-server` runtime gaps surfaced by the `uHOME v2` briefs
- requested by: `@dev/triage/complete/2026-03-16-uhome-server-empire-implementation-checklist.md`
- requested outcome: turn the remaining server-owned gaps from the `uHOME v2` master brief into explicit contracts, routes, tests, or scoped deferrals
- scope type: `cross-repo`
- owning repo or stream: `uHOME-server`
- binder: `#binder/uhome-server-v2-0-4-runtime-gap-pass`
- summary: close the highest-value server-owned gaps without broadening `uHOME-server` into Wizard control-plane ownership or downstream client-app ownership
- acceptance criteria:
  - a node-authority and failover contract is added with state-transition coverage, or a tracked deferral note is published in `docs/`
  - client capability registration and state surfaces are implemented, or `docs/clients/CLIENT-CAPABILITIES.md` is downgraded to a planned contract rather than a route-ready one
  - the server-side seam for Wizard-managed networking profiles (`Beacon`, `Crypt`, `Tomb`, `Home`) is defined as a server-consumable policy contract
  - quickstart and boundary docs clearly distinguish active server surfaces from deferred ones
- dependencies:
  - `@dev/triage/complete/2026-03-16-uhome-server-empire-implementation-checklist.md`
  - `uHOME-server` current Phase 5 and Phase 6 roadmap surfaces
  - `uDOS-wizard` current network-boundary and sibling-route docs
- boundary questions:
  - `uHOME-server` owns runtime fulfillment, local persistence, and local service composition
  - `uDOS-wizard` owns policy definition, credentials, and network control-plane behavior
  - `uHOME-matter` remains the owner for dedicated Matter and Home Assistant extension contracts outside transitional local support
- due or milestone: `v2.0.4 follow-up`

## Binder Fields

- state: `in-progress`
- owner: `uHOME-server`
- dependent repos:
  - `uDOS-wizard`
  - `uDOS-dev`
- blocked by:
  - none
- target branch: `develop`
- objective:
  - land the missing server-owned contracts needed to make the `uHOME v2` brief accurate at the runtime layer
- promotion criteria:
  - acceptance criteria are committed in `uHOME-server`
  - review-ready outcome is summarized in `@dev/submissions/`
- files or areas touched:
  - `uHOME-server/src/uhome_server/routes/`
  - `uHOME-server/src/uhome_server/cluster/`
  - `uHOME-server/docs/clients/`
  - `uHOME-server/docs/`
  - `uDOS-dev/@dev`

## Lifecycle Checklist

- [x] Open
- [x] Hand off
- [x] Advance
- [ ] Review
- [ ] Commit
- [ ] Complete
- [ ] Compile
- [ ] Promote
