# Repo Family Model

Status: active

This document defines how `uHOME-server` should read as a sibling pathway repo
inside the wider `uDOS` family.

## Shared Questions

Every sibling repo should answer the same onboarding questions in the same
order:

1. What pathway does this repo provide?
2. What Markdown or vault surfaces does it read or write?
3. What services does it expose?
4. What modules are optional?
5. How does it connect back to `uDOS-core`?

## Family Roles

### `uDOS-core`

Owns:

- core runtime
- shared contracts
- deterministic execution semantics
- family-wide education framing

### `uDOS-shell` and `uDOS-wizard`

Own:

- interactive shell and workspace surfaces
- provider, network, MCP, and assist workflows

### `uHOME-server`

Owns:

- local-network home infrastructure runtime
- household service model
- launcher and dashboard server control
- household vault examples and learning path
- `uHOME`-specific bundle and host-role contracts

### `uHOME-matter`

Owns:

- Matter and Home Assistant extension contracts
- local automation clone catalogs and target maps
- bridge-facing adapter definitions consumed by the server runtime

### `uHOME-empire`

Owns:

- remote sync and webhook workflows
- queueable automation or container-style job definitions
- online provider action templates and CRM-style console workflows

### `sonic-screwdriver`

Owns:

- deployment planning
- hardware bootstrap
- USB, rescue, and dual-boot install pathways
- generic install execution and hardware-facing workflows

### Client Repos

Own:

- Android, TV, and other device-native client implementations

## Boundary Rules

- `uHOME-server` is not a second core runtime beside `uDOS-core`
- `uHOME-server` should not absorb generic deployment ownership that belongs in
  `sonic-screwdriver`
- `sonic-screwdriver` should not redefine `uHOME` runtime architecture
- client implementations should consume stable server contracts rather than
  being embedded in this repo
- local automation contract ownership belongs in `uHOME-matter`, even when
  runtime support still exists in `uHOME-server`

## Integration Contract

`uHOME-server` connects back to `uDOS-core`, `uDOS-shell`, and `uDOS-wizard`
through:

- shared contracts and schemas
- workspace defaults and compatibility surfaces
- pathway documentation that uses the same architecture language
- install examples that remain compatible with `sonic-screwdriver`
