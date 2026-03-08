from __future__ import annotations

from pathlib import Path

from uhome_server.config import get_repo_root
from uhome_server.installer.bundle import read_bundle_manifest, verify_bundle


def test_example_standalone_bundle_verifies():
    bundle_dir = get_repo_root() / "examples" / "installer" / "bundles" / "standalone"
    manifest = read_bundle_manifest(bundle_dir)
    assert manifest is not None
    result = verify_bundle(manifest, bundle_dir)
    assert result.valid is True


def test_example_dual_boot_bundle_verifies():
    bundle_dir = get_repo_root() / "examples" / "installer" / "bundles" / "dual-boot"
    manifest = read_bundle_manifest(bundle_dir)
    assert manifest is not None
    result = verify_bundle(manifest, bundle_dir)
    assert result.valid is True
