# uHOME-server Getting Started

1. Review `docs/boundary.md` and `docs/base-runtime-boundary.md` so local runtime ownership stays inside `uHOME-server`.
2. Run `QUICKSTART.md` for the first runnable API, route checks, and Wizard pairing path.
3. Review `examples/basic-uhome-server-session.md` for the smallest standalone operator smoke.
4. Run the repo validation entrypoint before and after runtime changes:

```bash
bash scripts/run-uhome-server-checks.sh
```

1. Use `uDOS-wizard/docs/first-launch-quickstart.md` when validating workflow handoff into a running `uHOME-server`.
1. Use `uHOME-empire/docs/quickstart.md` when validating pack or sync handoff into the local runtime.
1. Keep service code under `services/` and `modules/`.
1. Route scheduling behavior through `scheduling/`.
1. Put new Matter or Home Assistant extension contracts in `uHOME-matter`.
1. Add tests before extending persistent behavior.
