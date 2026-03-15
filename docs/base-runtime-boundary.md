# uHOME-server Base Runtime Boundary

`uHOME-server` is the base runtime repo for the active `uHOME` v2 family.

## Owns

- host lifecycle and persistent local execution
- household services, scheduling, and playback surfaces
- base runtime profiles and checked-in server configuration examples
- LAN-first runtime routing and service composition

## Transitional Local Support

Some Home Assistant and bridge-oriented implementation still exists in this
repo for continuity with the existing runtime history. Treat that code as
runtime support owned by the server until it is intentionally migrated.

## Does Not Own

- Matter clone catalogs
- Home Assistant extension contracts
- platform UI ownership
- optional cloud sync or publishing workflows

Those surfaces belong in `uHOME-matter`, app repos, and `uHOME-empire`
respectively.
