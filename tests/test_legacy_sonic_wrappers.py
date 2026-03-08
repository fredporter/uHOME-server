from __future__ import annotations

import importlib
import sys
import warnings

from uhome_server.installer.bundle import read_bundle_manifest
from uhome_server.installer.plan import build_uhome_install_plan


def _import_legacy_module(module_name: str):
    sys.modules.pop(module_name, None)
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always", DeprecationWarning)
        module = importlib.import_module(module_name)
    return module, caught


def test_legacy_bundle_wrapper_warns_and_reexports():
    module, caught = _import_legacy_module("uhome_server.sonic.uhome_bundle")
    assert module.read_bundle_manifest is read_bundle_manifest
    assert any(
        str(item.message)
        == "uhome_server.sonic.uhome_bundle is deprecated; use uhome_server.installer.bundle instead."
        for item in caught
    )


def test_legacy_install_plan_wrapper_warns_and_reexports():
    module, caught = _import_legacy_module("uhome_server.sonic.uhome_installer")
    assert module.build_uhome_install_plan is build_uhome_install_plan
    assert any(
        str(item.message)
        == "uhome_server.sonic.uhome_installer is deprecated; use uhome_server.installer.plan instead."
        for item in caught
    )
