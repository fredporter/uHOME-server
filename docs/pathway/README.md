# Pathway

`uHOME-server` is the local-network home infrastructure pathway in the wider
`uDOS` family.

The pathway framing should stay consistent with sibling repos:

- `uDOS-core` = core runtime and shared contracts
- `uDOS-shell` / `uDOS-wizard` = interaction and assist surfaces
- `sonic-screwdriver` = deployment and hardware bootstrap
- `uHOME-server` = home infrastructure runtime and household service model
- `uHOME-matter` = local automation and bridge extension lane
- `uHOME-empire` = remote sync, webhook, and container-style workflow lane

This repo should not read like a second core and should not absorb generic
deployment ownership that belongs in `sonic-screwdriver`.
