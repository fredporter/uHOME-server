# uHOME-server Architecture

uHOME-server is the persistent local-service runtime for the family. In the
current product split it is the Linux-based uHOME host that owns the local
network runtime, Steam-side host role, and local vault-reader or Beacon
Activate content surfaces.

## Main Areas

- `services/` exposes runtime and service surfaces.
- `scheduling/` holds recurring execution logic.
- `modules/` organizes service modules and extensions.
- `config/` stores runtime configuration.
- `src/uhome_server/` remains the active standalone server package while the
  repo converges on the v2 spine.
- `scripts/run-uhome-server-checks.sh` is the activation validation entrypoint.

## Contract Edges

- `uDOS-core` defines canonical vault, task, workflow, and binder semantics.
- `uDOS-sonic-screwdriver` owns deployment, hardware bootstrap, and install
  planning into this runtime.
- `uDOS-wizard` provides network-facing contracts while `uHOME-server` owns the
  local-network runtime and local Beacon Activate content surfaces.
- `uHOME-empire` layers on top for Google and HubSpot sync plus console CRM and
  workflow management.
