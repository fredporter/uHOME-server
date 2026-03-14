"""uHOME presentation workflow service."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from uhome_server.config import read_json_file, utc_now_iso_z, write_json_file
from uhome_server.workspace import get_template_workspace_service

SUPPORTED_PRESENTATIONS = ("thin-gui", "steam-console")
SUPPORTED_NODE_ROLES = ("server", "tv-node")


class UHomePresentationService:
    def __init__(self, repo_root: Path):
        self.repo_root = repo_root
        self.state_dir = self.repo_root / "memory" / "wizard" / "uhome"
        self.state_path = self.state_dir / "presentation.json"
        self.state_dir.mkdir(parents=True, exist_ok=True)

    def _read_state(self) -> dict[str, Any]:
        return read_json_file(
            self.state_path,
            default={"active_presentation": None, "updated_at": None, "node_role": "server"},
        )

    def _write_state(self, payload: dict[str, Any]) -> None:
        write_json_file(self.state_path, payload, indent=2)

    def _workspace_fields(self) -> dict[str, str]:
        return get_template_workspace_service(self.repo_root).read_fields("settings", "uhome")

    def _preferred_presentation(self) -> tuple[str, str]:
        workspace_value = str(self._workspace_fields().get("presentation_mode") or "").strip().lower()
        if workspace_value in SUPPORTED_PRESENTATIONS:
            return workspace_value, "template_workspace"
        if workspace_value:
            return SUPPORTED_PRESENTATIONS[0], "template_workspace_invalid"
        return SUPPORTED_PRESENTATIONS[0], "default"

    def _node_role(self) -> tuple[str, str]:
        workspace_value = str(self._workspace_fields().get("node_role") or "").strip().lower().replace("_", "-")
        if workspace_value in SUPPORTED_NODE_ROLES:
            return workspace_value, "template_workspace"
        if workspace_value:
            return SUPPORTED_NODE_ROLES[0], "template_workspace_invalid"
        return SUPPORTED_NODE_ROLES[0], "default"

    def get_status(self) -> dict[str, Any]:
        state = self._read_state()
        preferred_presentation, preferred_presentation_source = self._preferred_presentation()
        node_role, node_role_source = self._node_role()
        return {
            "supported_presentations": list(SUPPORTED_PRESENTATIONS),
            "supported_node_roles": list(SUPPORTED_NODE_ROLES),
            "active_presentation": state.get("active_presentation"),
            "running": bool(state.get("active_presentation")),
            "preferred_presentation": preferred_presentation,
            "preferred_presentation_source": preferred_presentation_source,
            "node_role": node_role,
            "node_role_source": node_role_source,
            "state_path": str(self.state_path),
            "updated_at": state.get("updated_at"),
            "session_id": state.get("session_id"),
        }

    def _intent_payload(self, presentation: str | None, node_role: str, action: str) -> dict[str, Any]:
        launcher = presentation or self._preferred_presentation()[0]
        return {
            "intent": {
                "target": "uhome-console",
                "mode": "home",
                "launcher": launcher,
                "workspace": "uhome",
                "profile_id": node_role,
                "auth": {"wizard_mode_active": False, "uhome_role": node_role},
            },
            "action": action,
            "status": "ready" if action == "start" else "stopped",
        }

    def start(self, presentation: str) -> dict[str, Any]:
        normalized = (presentation or "").strip().lower()
        if not normalized:
            normalized, _ = self._preferred_presentation()
        if normalized not in SUPPORTED_PRESENTATIONS:
            raise ValueError(f"Unsupported uHOME presentation: {presentation}")
        node_role, _ = self._node_role()
        payload = {
            "active_presentation": normalized,
            "node_role": node_role,
            "updated_at": utc_now_iso_z(),
            "last_action": "start",
            "thin_gui": self._intent_payload(normalized, node_role, "start"),
        }
        self._write_state(payload)
        return payload

    def stop(self) -> dict[str, Any]:
        node_role, _ = self._node_role()
        payload = {
            "active_presentation": None,
            "node_role": node_role,
            "updated_at": utc_now_iso_z(),
            "last_action": "stop",
            "thin_gui": self._intent_payload(None, node_role, "stop"),
        }
        self._write_state(payload)
        return payload


def get_uhome_presentation_service(repo_root: Path) -> UHomePresentationService:
    return UHomePresentationService(repo_root=repo_root)
