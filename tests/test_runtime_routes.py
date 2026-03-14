from __future__ import annotations

from fastapi import FastAPI
from fastapi.testclient import TestClient

from uhome_server.routes import runtime as runtime_routes


def _client(monkeypatch) -> TestClient:
    monkeypatch.setattr(
        runtime_routes,
        "_repo_layout_status",
        lambda: {
            "repo_root": "/tmp/uhome-server",
            "exists": True,
            "missing_paths": [],
            "paths": {"defaults": "/tmp/uhome-server/defaults"},
        },
    )
    monkeypatch.setattr(
        runtime_routes,
        "_workspace_status",
        lambda: {
            "workspace_ref": "@memory/workspace/settings",
            "component_id": "uhome",
            "instructions_ref": "docs/workspace/instructions/uhome.md",
            "settings_keys": ["node_role", "presentation_mode"],
        },
    )
    monkeypatch.setattr(
        runtime_routes,
        "_config_status",
        lambda: {
            "config_path": "/tmp/uhome-server/memory/config/uhome.json",
            "legacy_config_path": "/tmp/uhome-server/memory/config/wizard.json",
            "active_config_path": "/tmp/uhome-server/memory/config/uhome.json",
            "active_config_exists": True,
            "legacy_config_fallback": False,
            "ha_bridge_enabled_env": False,
            "hdhomerun_host": "",
        },
    )
    monkeypatch.setattr(
        runtime_routes,
        "_ha_bridge_status",
        lambda: {"bridge": "uhome-ha", "enabled": False, "status": "disabled"},
    )
    monkeypatch.setattr(
        runtime_routes,
        "_jellyfin_status",
        lambda: {
            "jellyfin_configured": False,
            "jellyfin_reachable": False,
            "presentation_mode": "thin-gui",
            "preferred_target_client": "living-room",
            "note": "Set JELLYFIN_URL to enable live playback status.",
        },
    )
    app = FastAPI()
    app.include_router(runtime_routes.create_runtime_routes())
    return TestClient(app)


def test_runtime_readiness_reports_required_health(monkeypatch):
    client = _client(monkeypatch)
    response = client.get("/api/runtime/ready")
    assert response.status_code == 200
    body = response.json()
    assert body["ok"] is True
    assert body["status"] == "ready"
    assert body["checks"]["repo_layout"]["ok"] is True
    assert body["checks"]["config"]["ok"] is True
    assert body["checks"]["ha_bridge"]["required"] is False


def test_runtime_readiness_degrades_when_required_check_fails(monkeypatch):
    monkeypatch.setattr(
        runtime_routes,
        "_repo_layout_status",
        lambda: (_ for _ in ()).throw(RuntimeError("repo layout missing")),
    )
    monkeypatch.setattr(runtime_routes, "_config_status", lambda: {"active_config_exists": False})
    monkeypatch.setattr(runtime_routes, "_workspace_status", lambda: {"workspace_ref": "@memory/workspace/settings"})
    monkeypatch.setattr(runtime_routes, "_ha_bridge_status", lambda: {"enabled": True, "status": "ok"})
    monkeypatch.setattr(runtime_routes, "_jellyfin_status", lambda: {"jellyfin_configured": True, "jellyfin_reachable": True})
    app = FastAPI()
    app.include_router(runtime_routes.create_runtime_routes())
    client = TestClient(app)
    body = client.get("/api/runtime/ready").json()
    assert body["ok"] is False
    assert body["status"] == "degraded"
    assert body["checks"]["repo_layout"]["error"] == "repo layout missing"


def test_runtime_info_shape(monkeypatch):
    client = _client(monkeypatch)
    response = client.get("/api/runtime/info")
    assert response.status_code == 200
    body = response.json()
    assert body["app"] == "uHOME Server"
    assert "python_version" in body
    assert "platform" in body
    assert "settings" in body
