from __future__ import annotations

import json
from pathlib import Path

from uhome_server.cli import installer_main, launcher_main
from uhome_server.sonic.uhome_bundle import BUNDLE_SCHEMA_VERSION, UHOMEBundleComponent, UHOMEBundleManifest, write_bundle_manifest


def _write_probe(path: Path) -> None:
    path.write_text(
        json.dumps(
            {
                "cpu_cores": 6,
                "ram_gb": 16.0,
                "storage_gb": 512.0,
                "media_storage_gb": 4000.0,
                "has_gigabit": True,
                "has_hdmi": True,
                "tuner_count": 2,
                "has_usb_ports": 4,
                "has_bluetooth": True,
            }
        ),
        encoding="utf-8",
    )


def _write_bundle(bundle_dir: Path) -> None:
    artifact = bundle_dir / "components" / "jellyfin" / "payload.tar.gz"
    artifact.parent.mkdir(parents=True, exist_ok=True)
    artifact.write_bytes(b"uhome-artifact")
    import hashlib

    manifest = UHOMEBundleManifest(
        bundle_id="bundle-001",
        uhome_version="1.0.0",
        sonic_version="1.3.1",
        schema_version=BUNDLE_SCHEMA_VERSION,
        created_at="2026-03-08T00:00:00Z",
        components=[
            UHOMEBundleComponent(
                component_id="jellyfin",
                display_name="Jellyfin",
                version="10.9.0",
                artifact_path="components/jellyfin/payload.tar.gz",
                sha256=hashlib.sha256(b"uhome-artifact").hexdigest(),
                install_target="/opt/uhome/jellyfin",
            )
        ],
    )
    write_bundle_manifest(bundle_dir, manifest)


def test_launcher_cli_writes_state(tmp_path):
    code = launcher_main(["--repo-root", str(tmp_path), "start", "--presentation", "thin-gui"])
    assert code == 0
    state_path = tmp_path / "memory" / "wizard" / "uhome" / "presentation.json"
    payload = json.loads(state_path.read_text(encoding="utf-8"))
    assert payload["active_presentation"] == "thin-gui"


def test_launcher_cli_rejects_invalid_presentation(tmp_path):
    code = launcher_main(["--repo-root", str(tmp_path), "start", "--presentation", "bad-mode"])
    assert code == 2


def test_installer_preflight_cli(tmp_path):
    probe_path = tmp_path / "probe.json"
    _write_probe(probe_path)
    output_path = tmp_path / "preflight.json"
    code = installer_main(["preflight", "--probe", str(probe_path), "--output", str(output_path)])
    assert code == 0
    payload = json.loads(output_path.read_text(encoding="utf-8"))
    assert payload["passed"] is True


def test_installer_plan_cli(tmp_path):
    probe_path = tmp_path / "probe.json"
    bundle_dir = tmp_path / "bundle"
    _write_probe(probe_path)
    _write_bundle(bundle_dir)
    output_path = tmp_path / "plan.json"
    code = installer_main(
        [
            "plan",
            "--bundle-dir",
            str(bundle_dir),
            "--probe",
            str(probe_path),
            "--enable-ha-bridge",
            "--output",
            str(output_path),
        ]
    )
    assert code == 0
    payload = json.loads(output_path.read_text(encoding="utf-8"))
    assert payload["ready"] is True
    assert payload["preflight"]["passed"] is True


def test_installer_verify_bundle_cli_missing_manifest(tmp_path):
    output_path = tmp_path / "verify.json"
    code = installer_main(["verify-bundle", "--bundle-dir", str(tmp_path), "--output", str(output_path)])
    assert code == 1
    payload = json.loads(output_path.read_text(encoding="utf-8"))
    assert payload["valid"] is False


def test_installer_stage_cli(tmp_path):
    probe_path = tmp_path / "probe.json"
    bundle_dir = tmp_path / "bundle"
    stage_dir = tmp_path / "stage"
    _write_probe(probe_path)
    _write_bundle(bundle_dir)
    output_path = tmp_path / "stage-output.json"
    code = installer_main(
        [
            "stage",
            "--bundle-dir",
            str(bundle_dir),
            "--probe",
            str(probe_path),
            "--stage-dir",
            str(stage_dir),
            "--enable-ha-bridge",
            "--output",
            str(output_path),
        ]
    )
    assert code == 0
    payload = json.loads(output_path.read_text(encoding="utf-8"))
    assert payload["ready"] is True
    assert (stage_dir / "install-plan.json").exists()
    assert (stage_dir / "install-receipt.json").exists()
    assert (stage_dir / "install-state.json").exists()
    assert (stage_dir / "config" / "uhome.json").exists()
    assert (stage_dir / "components" / "jellyfin" / "payload.tar.gz").exists()
