# uHOME-server Base Runtime Boundary

`uHOME-server` is the `uHOME` service-stream repo for the active `uHOME` v2
family. It is not the primary family command-centre runtime host.

## Owns

- host lifecycle and persistent local execution
- household services, scheduling, and playback surfaces
- base runtime profiles and checked-in server configuration examples
- LAN-first runtime routing and service composition
- local console and ThinUI-oriented `uHOME` service surfaces

## Transitional Local Support

Some Home Assistant and bridge-oriented implementation still exists in this
repo for continuity with the existing runtime history. Treat that code as
runtime support owned by the server until it is intentionally migrated.

## Does Not Own

- the primary Ubuntu-hosted command-centre runtime
- Matter clone catalogs
- Home Assistant extension contracts
- platform UI ownership
- optional cloud sync or publishing workflows

Those surfaces belong in `uHOME-matter`, app repos, and `uDOS-empire`
respectively.
