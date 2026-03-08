"""CLI entrypoints for uHOME launchers and installers."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from uhome_server.config import get_repo_root
from uhome_server.services.uhome_presentation_service import get_uhome_presentation_service
from uhome_server.sonic.staging import stage_install_artifacts
from uhome_server.sonic.uhome_bundle import read_bundle_manifest, verify_bundle
from uhome_server.sonic.uhome_installer import UHOMEInstallOptions, build_uhome_install_plan
from uhome_server.sonic.uhome_preflight import preflight_check


def _read_json(path: str) -> dict[str, Any]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"Expected JSON object in {path}")
    return data


def _write_output(payload: dict[str, Any], out_path: str | None = None) -> None:
    rendered = json.dumps(payload, indent=2)
    if out_path:
        target = Path(out_path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(rendered + "\n", encoding="utf-8")
        return
    print(rendered)


def _launcher_repo_root(value: str | None) -> Path:
    return Path(value).expanduser().resolve() if value else get_repo_root()


def launcher_main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="uhome-launcher", description="Manage local uHOME presentation launchers.")
    parser.add_argument("--repo-root", help="Override the repository root for state and workspace access.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("status", help="Show current launcher status.")

    start_parser = subparsers.add_parser("start", help="Start a launcher presentation.")
    start_parser.add_argument("--presentation", default="", help="Presentation to start: thin-gui or steam-console.")

    subparsers.add_parser("stop", help="Stop the active launcher presentation.")

    args = parser.parse_args(argv)
    service = get_uhome_presentation_service(repo_root=_launcher_repo_root(args.repo_root))

    if args.command == "status":
        _write_output(service.get_status())
        return 0
    if args.command == "start":
        try:
            _write_output(service.start(args.presentation))
            return 0
        except ValueError as exc:
            _write_output({"success": False, "error": str(exc)})
            return 2
    if args.command == "stop":
        _write_output(service.stop())
        return 0
    parser.error(f"Unsupported launcher command: {args.command}")
    return 2


def installer_main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="uhome-installer", description="Build and inspect uHOME install plans.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    preflight_parser = subparsers.add_parser("preflight", help="Run hardware preflight against a JSON probe.")
    preflight_parser.add_argument("--probe", required=True, help="Path to a hardware probe JSON object.")
    preflight_parser.add_argument("--output", help="Optional path to write the JSON result.")

    verify_parser = subparsers.add_parser("verify-bundle", help="Verify bundle artifacts against the manifest.")
    verify_parser.add_argument("--bundle-dir", required=True, help="Directory containing uhome-bundle.json.")
    verify_parser.add_argument("--output", help="Optional path to write the JSON result.")

    plan_parser = subparsers.add_parser("plan", help="Build a uHOME install plan from a bundle and hardware probe.")
    plan_parser.add_argument("--bundle-dir", required=True, help="Directory containing uhome-bundle.json.")
    plan_parser.add_argument("--probe", required=True, help="Path to a hardware probe JSON object.")
    plan_parser.add_argument("--install-root", default="/opt/uhome", help="Install root used for the generated plan.")
    plan_parser.add_argument("--kiosk-user", default="uhome", help="Autologin kiosk user.")
    plan_parser.add_argument("--enable-ha-bridge", action="store_true", help="Enable Home Assistant bridge config steps.")
    plan_parser.add_argument(
        "--disable-autologin-kiosk",
        action="store_true",
        help="Skip kiosk autologin enablement steps.",
    )
    plan_parser.add_argument("--dry-run", action="store_true", help="Mark the plan as a dry run.")
    plan_parser.add_argument("--output", help="Optional path to write the JSON result.")

    stage_parser = subparsers.add_parser("stage", help="Materialize a staged installer directory.")
    stage_parser.add_argument("--bundle-dir", required=True, help="Directory containing uhome-bundle.json.")
    stage_parser.add_argument("--probe", required=True, help="Path to a hardware probe JSON object.")
    stage_parser.add_argument("--stage-dir", required=True, help="Output directory for staged artifacts.")
    stage_parser.add_argument("--install-root", default="/opt/uhome", help="Install root used for the staged artifacts.")
    stage_parser.add_argument("--kiosk-user", default="uhome", help="Autologin kiosk user.")
    stage_parser.add_argument("--enable-ha-bridge", action="store_true", help="Enable Home Assistant bridge config artifacts.")
    stage_parser.add_argument(
        "--disable-autologin-kiosk",
        action="store_true",
        help="Skip kiosk autologin enablement artifacts.",
    )
    stage_parser.add_argument("--dry-run", action="store_true", help="Mark the generated plan as a dry run.")
    stage_parser.add_argument("--output", help="Optional path to write the JSON result.")

    args = parser.parse_args(argv)

    if args.command == "preflight":
        result = preflight_check(_read_json(args.probe))
        _write_output(result.to_dict(), args.output)
        return 0 if result.passed else 1

    bundle_dir = Path(args.bundle_dir).expanduser().resolve()

    if args.command == "verify-bundle":
        manifest = read_bundle_manifest(bundle_dir)
        if manifest is None:
            _write_output({"valid": False, "missing": ["uhome-bundle.json"], "corrupt": [], "warnings": []}, args.output)
            return 1
        result = verify_bundle(manifest, bundle_dir)
        _write_output(
            {"valid": result.valid, "missing": result.missing, "corrupt": result.corrupt, "warnings": result.warnings},
            args.output,
        )
        return 0 if result.valid else 1

    if args.command == "plan":
        opts = UHOMEInstallOptions(
            install_root=args.install_root,
            enable_autologin_kiosk=not args.disable_autologin_kiosk,
            kiosk_user=args.kiosk_user,
            enable_ha_bridge=args.enable_ha_bridge,
            dry_run=args.dry_run,
        )
        plan = build_uhome_install_plan(bundle_dir, _read_json(args.probe), opts)
        _write_output(plan.to_dict(), args.output)
        return 0 if plan.ready else 1

    if args.command == "stage":
        opts = UHOMEInstallOptions(
            install_root=args.install_root,
            enable_autologin_kiosk=not args.disable_autologin_kiosk,
            kiosk_user=args.kiosk_user,
            enable_ha_bridge=args.enable_ha_bridge,
            dry_run=args.dry_run,
        )
        try:
            plan, staged = stage_install_artifacts(
                bundle_dir,
                Path(args.stage_dir).expanduser().resolve(),
                _read_json(args.probe),
                opts,
            )
        except ValueError as exc:
            _write_output({"ready": False, "error": str(exc)}, args.output)
            return 1
        _write_output({"ready": plan.ready, "plan": plan.to_dict(), "staged": staged.to_dict()}, args.output)
        return 0

    parser.error(f"Unsupported installer command: {args.command}")
    return 2


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="uhome", description="uHOME operator CLI.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("launcher", help="Manage local launcher state.")
    subparsers.add_parser("installer", help="Manage install plans and preflight.")
    args, remaining = parser.parse_known_args(argv)
    if args.command == "launcher":
        return launcher_main(remaining)
    if args.command == "installer":
        return installer_main(remaining)
    parser.error(f"Unsupported command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
