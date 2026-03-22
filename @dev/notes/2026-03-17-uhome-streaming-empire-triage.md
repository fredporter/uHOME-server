# Triage: uHOME v2 Streaming and Empire Briefs

- date: 2026-03-17
- source briefs:
  - @dev/inbox/briefs/uhome_v_2_streaming_brief.md
  - @dev/inbox/briefs/uhome_v_2_empire.md
  - @dev/inbox/briefs/uhome_v_2_master_spec.md
- triaged by: @dev/ubuntu-base-image intake pass

## Scope Decision

Streaming brief is implementation-ready and scoped to uHOME-server. Target: v2.0.7 Round A.

Empire brief is positioning and boundary documentation. No new implementation scope
breaks from the current repo layout. Absorb into architectural record; not a separate
round.

Master spec is architectural context. Absorbed into the streaming round as background.

## Streaming Brief — Normalized Scope

Owner: uHOME-server  
Binder: #binder/uhome-server-v2-0-7-streaming-channels  
Target: v2.0.7 Round A

Scope:
- source adapter layer: channel.rewind.mtv and channel.rewind.cartoons adapters
- session controller: per-room session registry with join/create/sync/resume/move
- local stream gateway: web passthrough + proxy-assisted modes as baseline
- client contract: local channel list, session state, and handoff endpoints
- boundary: uHOME-server owns local delivery orchestration, not channel ownership

Out of scope for Round A:
- transcoded relay mode (future)
- full CDN or restreaming stack
- mobile app UI (consumes contracts only)

## Empire Brief — Disposition

Empire boundary is already correctly documented in docs and repo-family-map.
No implementation change required. Empire brief is absorbed as architectural context
and archived to triage/complete.

## Routing

- streaming brief → v2.0.7 Round A binder in @dev/requests/
- empire brief → archived, no separate binder
- master spec → architectural reference for streaming round
