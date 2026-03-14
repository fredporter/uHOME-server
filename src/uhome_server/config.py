"""Local config, path, and bootstrap helpers for standalone uHOME services."""

from __future__ import annotations

import json
import logging
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any


def get_logger(name: str) -> logging.Logger:
    logging.basicConfig(level=logging.INFO)
    return logging.getLogger(name)


def get_repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def utc_now_iso_z() -> str:
    from datetime import datetime, timezone

    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


@dataclass(frozen=True)
class RuntimeSettings:
    repo_root: Path
    memory_root: Path
    config_dir: Path
    config_path: Path
    legacy_config_path: Path
    workspace_settings_dir: Path
    uhome_bank_dir: Path
    jellyfin_url: str
    jellyfin_api_key: str
    hdhomerun_host: str
    ha_bridge_enabled: bool

    def to_dict(self) -> dict[str, Any]:
        return {
            "repo_root": str(self.repo_root),
            "memory_root": str(self.memory_root),
            "config_dir": str(self.config_dir),
            "config_path": str(self.config_path),
            "legacy_config_path": str(self.legacy_config_path),
            "workspace_settings_dir": str(self.workspace_settings_dir),
            "uhome_bank_dir": str(self.uhome_bank_dir),
            "jellyfin_url": self.jellyfin_url,
            "jellyfin_api_key_configured": bool(self.jellyfin_api_key),
            "hdhomerun_host": self.hdhomerun_host,
            "ha_bridge_enabled": self.ha_bridge_enabled,
        }


def _env_bool(name: str, default: bool = False) -> bool:
    raw = str(os.environ.get(name, "")).strip().lower()
    if not raw:
        return default
    return raw in {"1", "true", "yes", "on"}


def get_runtime_settings(repo_root: Path | None = None) -> RuntimeSettings:
    repo_root = repo_root or get_repo_root()
    memory_root = repo_root / "memory"
    config_dir = memory_root / "config"
    config_path = config_dir / "uhome.json"
    legacy_config_path = config_dir / "wizard.json"
    workspace_settings_dir = memory_root / "workspace" / "settings"
    uhome_bank_dir = memory_root / "bank" / "uhome"
    return RuntimeSettings(
        repo_root=repo_root,
        memory_root=memory_root,
        config_dir=config_dir,
        config_path=config_path,
        legacy_config_path=legacy_config_path,
        workspace_settings_dir=workspace_settings_dir,
        uhome_bank_dir=uhome_bank_dir,
        jellyfin_url=str(os.environ.get("JELLYFIN_URL", "") or "").strip(),
        jellyfin_api_key=str(os.environ.get("JELLYFIN_API_KEY", "") or "").strip(),
        hdhomerun_host=str(os.environ.get("HDHOMERUN_HOST", "") or "").strip(),
        ha_bridge_enabled=_env_bool("HA_BRIDGE_ENABLED", False),
    )


def bootstrap_runtime(repo_root: Path | None = None) -> dict[str, Any]:
    settings = get_runtime_settings(repo_root)
    created_paths: list[str] = []
    for path in (
        settings.memory_root,
        settings.config_dir,
        settings.workspace_settings_dir,
        settings.uhome_bank_dir,
    ):
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
            created_paths.append(str(path))

    active_config_path = settings.config_path
    if not active_config_path.exists() and settings.legacy_config_path.exists():
        active_config_path = settings.legacy_config_path

    return {
        "ok": True,
        "timestamp": utc_now_iso_z(),
        "created_paths": created_paths,
        "settings": settings.to_dict(),
        "active_config_path": str(active_config_path),
        "active_config_exists": active_config_path.exists(),
        "legacy_config_fallback": active_config_path == settings.legacy_config_path,
    }


class JSONConfigStore:
    def __init__(self, path: Path | None = None):
        settings = get_runtime_settings()
        self.path = path or settings.config_path
        self.legacy_path = self.path.with_name("wizard.json") if path is not None else settings.legacy_config_path

    def _load(self) -> dict[str, Any]:
        active_path = self.path if self.path.exists() else self.legacy_path
        if not active_path.exists():
            return {}
        try:
            return json.loads(active_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return {}

    def get(self, key: str, default: Any = None) -> Any:
        if key in os.environ:
            return os.environ[key]
        return self._load().get(key, default)

    def set(self, key: str, value: Any) -> None:
        payload = self._load()
        payload[key] = value
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def read_json_file(path: Path, default: dict[str, Any]) -> dict[str, Any]:
    if not path.exists():
        return default
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            return data
    except json.JSONDecodeError:
        pass
    return default


def write_json_file(path: Path, payload: dict[str, Any], indent: int = 2) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=indent), encoding="utf-8")
