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
5. How does it connect back to `uDOS` core?

## Family Roles

### `uDOS`

Owns:

- core runtime
- shared contracts
- Wizard and other main interaction surfaces
- family-wide education framing

### `uHOME-server`

Owns:

- local-network home infrastructure runtime
- household service model
- launcher and dashboard server control
- household vault examples and learning path
- `uHOME`-specific bundle and host-role contracts

### `uDOS-sonic`

Owns:

- deployment planning
- hardware bootstrap
- USB, rescue, and dual-boot install pathways
- generic install execution and hardware-facing workflows

### Client Repos

Own:

- Android, TV, and other device-native client implementations

## Boundary Rules

- `uHOME-server` is not a second core runtime beside `uDOS`
- `uHOME-server` should not absorb generic deployment ownership that belongs in
  `uDOS-sonic`
- `uDOS-sonic` should not redefine `uHOME` runtime architecture
- client implementations should consume stable server contracts rather than
  being embedded in this repo

## Integration Contract

`uHOME-server` connects back to `uDOS` through:

- shared contracts and schemas
- workspace defaults and compatibility surfaces
- pathway documentation that uses the same architecture language
- install examples that remain compatible with `uDOS-sonic`
