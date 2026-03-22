# Request: #binder/uhome-server-v2-0-7-streaming-channels

- title: uHOME-server local streaming channel ingestion lane
- requested by: @dev/uhome-streaming
- owning repo or stream: uHOME-server
- binder: #binder/uhome-server-v2-0-7-streaming-channels
- summary: Stand up the source adapter layer, session controller, and local stream
  gateway in uHOME-server so household clients can consume MTV Rewind and Cartoon
  Rewind as local always-on channels.
- acceptance criteria:
  - channel source adapters defined for channel.rewind.mtv and channel.rewind.cartoons
  - session controller supports join, create, sync, resume, and move operations
  - local stream gateway exposes web-passthrough and proxy-assisted modes
  - REST API routes expose channel list, session state, and session actions
  - test coverage for service layer and route layer
  - uHOME-server test suite passes
- dependencies:
  - uHOME-server existing playback and household service lanes
- due or milestone: v2.0.7 Round A

## Binder Fields

- state: in-progress
- owner: uHOME-server
- dependent repos:
  - uHOME-server
  - uDOS-dev
- blocked by:
  - none
- target branch: develop
- objective:
  - implement the streaming channel service layer and client-facing REST surface
    as the first uHOME-server media channel activation pass

## Boundary Rules

- uHOME-server owns local delivery orchestration, not channel ownership
- upstream channels remain the source of truth
- clients connect to uHOME-server first, not directly to the public site
- no CDN, restreaming, or pirate-media hosting in scope
- transcoded relay mode is out of scope for Round A

## Lifecycle Checklist

- [x] Open
- [x] Hand off
- [x] Advance
- [x] Review
- [x] Commit
- [x] Complete
- [x] Compile
- [ ] Promote
