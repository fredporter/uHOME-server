"""Runtime readiness and environment routes for the standalone uHOME server."""

from __future__ import annotations

import platform
import sys
from pathlib import Path
from typing import Any, Callable, Optional

from fastapi import APIRouter, Depends, Request

from uhome_server.config import get_repo_root, get_runtime_settings, utc_now_iso_z
from uhome_server.services.home_assistant_service import get_ha_service
from uhome_server.services.uhome_command_handlers import playback_status
from uhome_server.workspace import get_template_workspace_service


def _probe(fn: Callable[[], dict[str, Any]], label: str, required: bool = True) -> dict[str, Any]:
    try:
        result = fn()
        payload = result if isinstance(result, dict) else {"result": result}
        return {"ok": True, "required": required, "subsystem": label, **payload}
    except Exception as exc:
        return {"ok": False, "required": required, "subsystem": label, "error": str(exc)}


def _repo_layout_status() -> dict[str, Any]:
    repo_root = get_repo_root()
    expected_paths = {
        "defaults": repo_root / "defaults",
        "library": repo_root / "library",
        "docs": repo_root / "docs",
        "src": repo_root / "src",
    }
    missing = [name for name, path in expected_paths.items() if not path.exists()]
    return {
        "repo_root": str(repo_root),
        "exists": repo_root.exists(),
        "missing_paths": missing,
        "paths": {name: str(path) for name, path in expected_paths.items()},
    }


def _workspace_status() -> dict[str, Any]:
    workspace = get_template_workspace_service(get_repo_root())
    snapshot = workspace.component_snapshot("uhome")
    settings = snapshot.get("settings", {})
    return {
        "workspace_ref": "@memory/workspace/settings",
        "component_id": "uhome",
        "instructions_ref": snapshot.get("instructions_ref"),
        "settings_keys": sorted(settings.keys()),
    }


def _ha_bridge_status() -> dict[str, Any]:
    return get_ha_service().status()


def _jellyfin_status() -> dict[str, Any]:
    status = playback_status({})
    return {
        "jellyfin_configured": status.get("jellyfin_configured", False),
        "jellyfin_reachable": status.get("jellyfin_reachable", False),
        "presentation_mode": status.get("presentation_mode"),
        "preferred_target_client": status.get("preferred_target_client"),
        "issue": status.get("issue"),
        "note": status.get("note"),
    }


def _config_status() -> dict[str, Any]:
    settings = get_runtime_settings(get_repo_root())
    active_config_path = settings.config_path if settings.config_path.exists() else settings.legacy_config_path
    return {
        "config_path": str(settings.config_path),
        "legacy_config_path": str(settings.legacy_config_path),
        "active_config_path": str(active_config_path),
        "active_config_exists": active_config_path.exists(),
        "legacy_config_fallback": active_config_path == settings.legacy_config_path,
        "ha_bridge_enabled_env": settings.ha_bridge_enabled,
        "hdhomerun_host": settings.hdhomerun_host,
    }


def runtime_readiness_probe() -> dict[str, Any]:
    checks = {
        "repo_layout": _probe(_repo_layout_status, "repo_layout"),
        "config": _probe(_config_status, "config"),
        "workspace": _probe(_workspace_status, "workspace"),
        "ha_bridge": _probe(_ha_bridge_status, "ha_bridge", required=False),
        "jellyfin": _probe(_jellyfin_status, "jellyfin", required=False),
    }
    required_checks = [item for item in checks.values() if item.get("required")]
    optional_checks = [item for item in checks.values() if not item.get("required")]
    required_ok = all(item.get("ok", False) for item in required_checks)
    optional_ok = sum(1 for item in optional_checks if item.get("ok", False))
    return {
        "ok": required_ok,
        "status": "ready" if required_ok else "degraded",
        "timestamp": utc_now_iso_z(),
        "checks": checks,
        "summary": {
            "required_total": len(required_checks),
            "required_healthy": sum(1 for item in required_checks if item.get("ok", False)),
            "optional_total": len(optional_checks),
            "optional_healthy": optional_ok,
        },
    }


def runtime_info() -> dict[str, Any]:
    repo_root = get_repo_root()
    settings = get_runtime_settings(repo_root)
    return {
        "app": "uHOME Server",
        "timestamp": utc_now_iso_z(),
        "python_version": sys.version.split()[0],
        "platform": platform.system().lower(),
        "platform_release": platform.release(),
        "repo_root": str(repo_root),
        "cwd": str(Path.cwd()),
        "settings": settings.to_dict(),
    }


def create_runtime_routes(auth_guard: Optional[Callable] = None) -> APIRouter:
    dependencies = [Depends(auth_guard)] if auth_guard else []
    router = APIRouter(prefix="/api/runtime", tags=["runtime"])

    @router.get("/ready")
    async def readiness():
        return runtime_readiness_probe()

    @router.get("/info", dependencies=dependencies)
    async def info(request: Request):
        payload = runtime_info()
        bootstrap = getattr(request.app.state, "bootstrap", None)
        if isinstance(bootstrap, dict):
            payload["bootstrap"] = bootstrap
        return payload

    return router
