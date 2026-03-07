# uHOME Server Status

Status: active migration
Updated: 2026-03-07

## Summary

The standalone `uHOME Server` repository now contains the first extracted
service and contract modules migrated from `uDOS`.

## Current Focus

- stabilize the extracted Home Assistant and presentation API surfaces
- preserve the migrated Sonic install/bundle contracts
- continue moving `uHOME`-owned docs and runtime code out of `uDOS`

## Next Steps

- add dependency lockfiles and CI for the standalone package
- migrate any remaining `uHOME`-owned runtime modules that no longer belong in `uDOS`
- replace file-backed placeholders with durable service storage where needed
- document deployment, packaging, and release flows for standalone installs
