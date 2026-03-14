# Course 05 - Configurable Webhook Server

Purpose:

- explain how `uHOME-empire` handles online API calls, webhooks, and cron-type
  sync jobs
- keep online service integrations separate from local household automation in
  `uHOME-server`

Topics:

- configurable webhook receivers
- scheduled outbound API calls
- Google Docs, Keep, and Tasks sync points
- HubSpot contact and task sync
- reusable templates for new online providers

Repo anchors:

- sibling repo: `uHOME-empire/src/webhooks/`
- sibling repo: `uHOME-empire/examples/configurable-webhook-server.json`
- sibling repo: `uHOME-empire/docs/architecture.md`
- `../../docs/pathway/REPO-FAMILY.md`

Boundary note:

- `uHOME-server` owns Home Assistant, Matter, and local automation pathways
- `uHOME-empire` owns custom online APIs, webhooks, and always-on sync jobs

First project:

- build a configurable webhook job that reads vault state, receives an inbound
  trigger, and pushes a reviewed update into a remote API
