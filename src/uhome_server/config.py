"""Local config and repo-root helpers for standalone uHOME services."""

from __future__ import annotations

import json
import logging
import os
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


class JSONConfigStore:
    def __init__(self, path: Path | None = None):
        self.path = path or (get_repo_root() / "memory" / "config" / "wizard.json")

    def _load(self) -> dict[str, Any]:
        if not self.path.exists():
            return {}
        try:
            return json.loads(self.path.read_text(encoding="utf-8"))
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
