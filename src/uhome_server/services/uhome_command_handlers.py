"""Standalone uHOME command handlers extracted from uDOS."""

from __future__ import annotations

import json
import socket
import urllib.request
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from uhome_server.config import JSONConfigStore, get_logger, get_repo_root
from uhome_server.workspace import get_template_workspace_service

_log = get_logger("uhome.command-handlers")
_config = JSONConfigStore()


def _dvr_schedule_path() -> Path:
    return get_repo_root() / "memory" / "bank" / "uhome" / "dvr_schedule.json"


def _playback_queue_path() -> Path:
    return get_repo_root() / "memory" / "bank" / "uhome" / "playback_queue.json"


def _load_json_list(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, list):
            return data
    except json.JSONDecodeError:
        pass
    return []


def _save_json_list(path: Path, payload: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def tuner_discover(params: dict[str, Any]) -> dict[str, Any]:
    devices: list[dict[str, Any]] = []
    candidates = [params.get("host") or "hdhomerun.local", "192.168.1.1"]
    env_host = str(_config.get("HDHOMERUN_HOST", "") or "").strip()
    if env_host:
        candidates.insert(0, env_host)

    for host in dict.fromkeys(candidates):
        try:
            ip = socket.gethostbyname(host)
            with urllib.request.urlopen(f"http://{ip}/discover.json", timeout=2) as resp:
                data = json.loads(resp.read())
            devices.append(
                {
                    "host": ip,
                    "device_id": data.get("DeviceID"),
                    "friendly_name": data.get("FriendlyName", "HDHomeRun"),
                    "model": data.get("ModelNumber"),
                    "tuner_count": data.get("TunerCount", 1),
                    "firmware": data.get("FirmwareVersion"),
                    "base_url": data.get("BaseURL"),
                }
            )
        except Exception as exc:
            _log.debug("tuner_discover: %s unreachable: %s", host, exc)

    return {"command": "uhome.tuner.discover", "devices_found": len(devices), "devices": devices}


def tuner_status(params: dict[str, Any]) -> dict[str, Any]:
    host = str(params.get("host") or _config.get("HDHOMERUN_HOST", "") or "hdhomerun.local").strip()
    result: dict[str, Any] = {
        "command": "uhome.tuner.status",
        "host": host,
        "reachable": False,
        "channels": [],
    }
    try:
        ip = socket.gethostbyname(host)
        with urllib.request.urlopen(f"http://{ip}/discover.json", timeout=2) as resp:
            data = json.loads(resp.read())
        result.update(
            {
                "reachable": True,
                "device_id": data.get("DeviceID"),
                "model": data.get("ModelNumber"),
                "tuner_count": data.get("TunerCount", 1),
            }
        )
    except Exception as exc:
        result["issue"] = str(exc)
    return result


def dvr_list_rules(params: dict[str, Any]) -> dict[str, Any]:
    rules = _load_json_list(_dvr_schedule_path())
    return {"command": "uhome.dvr.list_rules", "rule_count": len(rules), "rules": rules}


def dvr_schedule(params: dict[str, Any]) -> dict[str, Any]:
    title = str(params.get("title") or "").strip()
    if not title:
        return {"command": "uhome.dvr.schedule", "success": False, "error": "title is required"}

    rule = {
        "id": str(uuid.uuid4())[:8],
        "title": title,
        "channel": params.get("channel"),
        "start_time": params.get("start_time"),
        "duration_minutes": params.get("duration_minutes"),
        "repeat": params.get("repeat", "none"),
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    rules = _load_json_list(_dvr_schedule_path())
    rules.append(rule)
    _save_json_list(_dvr_schedule_path(), rules)
    return {"command": "uhome.dvr.schedule", "success": True, "rule": rule}


def dvr_cancel(params: dict[str, Any]) -> dict[str, Any]:
    rule_id = str(params.get("id") or "").strip()
    if not rule_id:
        return {"command": "uhome.dvr.cancel", "success": False, "error": "id is required"}
    rules = _load_json_list(_dvr_schedule_path())
    before = len(rules)
    remaining = [rule for rule in rules if rule.get("id") != rule_id]
    _save_json_list(_dvr_schedule_path(), remaining)
    removed = before - len(remaining)
    return {"command": "uhome.dvr.cancel", "success": removed > 0, "removed": removed, "id": rule_id}


_AD_MODE_KEY = "uhome_ad_processing_mode"
_AD_MODE_FIELD = "ad-processing-mode"
_AD_MODES = {"disabled", "comskip_auto", "comskip_manual", "passthrough"}
_PRESENTATION_MODES = {"thin-gui", "steam-console"}
_DEFAULT_PRESENTATION_MODE = "thin-gui"
_DEFAULT_TARGET_CLIENT = "living-room"


def ad_get_mode(params: dict[str, Any]) -> dict[str, Any]:
    mode = "disabled"
    source = "default"
    try:
        fields = get_template_workspace_service().read_fields("settings", "uhome")
        workspace_mode = str(fields.get("ad_processing_mode") or "").strip().lower()
        if workspace_mode in _AD_MODES:
            mode = workspace_mode
            source = "template_workspace"
        elif workspace_mode:
            source = "template_workspace_invalid"
    except Exception:
        pass

    if source != "template_workspace":
        config_mode = str(_config.get(_AD_MODE_KEY, mode) or mode).strip().lower()
        if config_mode in _AD_MODES:
            mode = config_mode
            source = "wizard_config"

    return {
        "command": "uhome.ad_processing.get_mode",
        "mode": mode,
        "source": source,
        "valid_modes": sorted(_AD_MODES),
    }


def ad_set_mode(params: dict[str, Any]) -> dict[str, Any]:
    mode = str(params.get("mode") or "").strip().lower()
    if mode not in _AD_MODES:
        return {
            "command": "uhome.ad_processing.set_mode",
            "success": False,
            "error": f"invalid mode {mode!r}; valid: {sorted(_AD_MODES)}",
        }
    try:
        get_template_workspace_service().write_user_field("settings", "uhome", _AD_MODE_FIELD, mode)
        _config.set(_AD_MODE_KEY, mode)
    except Exception as exc:
        return {"command": "uhome.ad_processing.set_mode", "success": False, "error": str(exc)}
    return {"command": "uhome.ad_processing.set_mode", "success": True, "mode": mode, "source": "template_workspace"}


def _jellyfin_base_url() -> str:
    return str(_config.get("JELLYFIN_URL", "") or "").strip()


def _uhome_workspace_fields() -> dict[str, str]:
    return get_template_workspace_service().read_fields("settings", "uhome")


def _workspace_choice(
    workspace_fields: dict[str, str],
    field_name: str,
    default: str,
    valid_values: set[str] | None = None,
) -> tuple[str, str]:
    raw_value = str(workspace_fields.get(field_name) or "").strip()
    if not raw_value:
        return default, "default"
    value = raw_value.lower() if valid_values is not None else raw_value
    if valid_values is not None and value not in valid_values:
        return default, "template_workspace_invalid"
    return value, "template_workspace"


def playback_status(params: dict[str, Any]) -> dict[str, Any]:
    workspace_fields = _uhome_workspace_fields()
    presentation_mode, presentation_mode_source = _workspace_choice(
        workspace_fields, "presentation_mode", _DEFAULT_PRESENTATION_MODE, valid_values=_PRESENTATION_MODES
    )
    preferred_target_client, preferred_target_client_source = _workspace_choice(
        workspace_fields, "preferred_target_client", _DEFAULT_TARGET_CLIENT
    )
    base_url = _jellyfin_base_url()
    result: dict[str, Any] = {
        "command": "uhome.playback.status",
        "jellyfin_configured": bool(base_url),
        "active_sessions": [],
        "presentation_mode": presentation_mode,
        "presentation_mode_source": presentation_mode_source,
        "preferred_target_client": preferred_target_client,
        "preferred_target_client_source": preferred_target_client_source,
    }
    if not base_url:
        result["note"] = "Set JELLYFIN_URL to enable live playback status."
        return result

    try:
        api_key = str(_config.get("JELLYFIN_API_KEY", "") or "")
        url = f"{base_url.rstrip('/')}/Sessions?api_key={api_key}"
        with urllib.request.urlopen(url, timeout=3) as resp:
            sessions = json.loads(resp.read())
        active = [session for session in sessions if session.get("NowPlayingItem")]
        result["active_sessions"] = [
            {
                "user": session.get("UserName"),
                "title": session.get("NowPlayingItem", {}).get("Name"),
                "media_type": session.get("NowPlayingItem", {}).get("Type"),
                "client": session.get("Client"),
            }
            for session in active
        ]
        result["jellyfin_reachable"] = True
    except Exception as exc:
        result["jellyfin_reachable"] = False
        result["issue"] = str(exc)
    return result


def playback_handoff(params: dict[str, Any]) -> dict[str, Any]:
    item_id = str(params.get("item_id") or "").strip()
    workspace_fields = _uhome_workspace_fields()
    default_target, default_target_source = _workspace_choice(
        workspace_fields, "preferred_target_client", _DEFAULT_TARGET_CLIENT
    )
    requested_target = str(params.get("target_client") or "").strip()
    use_default_target = not requested_target or requested_target.lower() == "default"
    target_client = default_target if use_default_target else requested_target
    if not item_id:
        return {"command": "uhome.playback.handoff", "success": False, "error": "item_id is required"}

    try:
        queue = _load_json_list(_playback_queue_path())
        queue.append(
            {
                "id": str(uuid.uuid4())[:8],
                "item_id": item_id,
                "target_client": target_client,
                "queued_at": datetime.now(timezone.utc).isoformat(),
                "params": {k: v for k, v in params.items() if k not in {"item_id", "target_client"}},
            }
        )
        _save_json_list(_playback_queue_path(), queue)
        return {
            "command": "uhome.playback.handoff",
            "success": True,
            "item_id": item_id,
            "target_client": target_client,
            "source": default_target_source if use_default_target else "request",
        }
    except Exception as exc:
        return {"command": "uhome.playback.handoff", "success": False, "error": str(exc)}


_HANDLERS = {
    "uhome.tuner.discover": tuner_discover,
    "uhome.tuner.status": tuner_status,
    "uhome.dvr.list_rules": dvr_list_rules,
    "uhome.dvr.schedule": dvr_schedule,
    "uhome.dvr.cancel": dvr_cancel,
    "uhome.ad_processing.get_mode": ad_get_mode,
    "uhome.ad_processing.set_mode": ad_set_mode,
    "uhome.playback.status": playback_status,
    "uhome.playback.handoff": playback_handoff,
}


def dispatch(command: str, params: dict[str, Any]) -> dict[str, Any]:
    handler = _HANDLERS.get(command)
    if handler is None:
        raise KeyError(f"No handler for uHOME command: {command!r}")
    return handler(params)
