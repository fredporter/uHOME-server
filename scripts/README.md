# Scripts

The `scripts/` root is reserved for checked-in operational tooling that belongs
to `uHOME-server`.

Current state:

- most deployment and install mechanics still live in `src/uhome_server/sonic/`
- generated host-apply scripts are produced during installer execution

Boundary rule:

- generic deployment bootstrap should converge toward
  `uDOS-sonic-screwdriver`
- `uHOME-server` should keep only server-owned scripts and host-role helpers
