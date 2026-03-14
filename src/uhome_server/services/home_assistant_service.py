"""Standalone Home Assistant bridge service."""

from __future__ import annotations

from typing import Any

from uhome_server.config import JSONConfigStore

_BRIDGE_VERSION = "0.1.0"

_COMMAND_ALLOWLIST: set[str] = {
    "uhome.tuner.discover",
    "uhome.tuner.status",
    "uhome.dvr.list_rules",
    "uhome.dvr.schedule",
    "uhome.dvr.cancel",
    "uhome.ad_processing.get_mode",
    "uhome.ad_processing.set_mode",
    "uhome.playback.handoff",
    "uhome.playback.status",
    "system.info",
    "system.capabilities",
}


class HomeAssistantService:
    """uHOME server ↔ Home Assistant bridge service."""

    def __init__(self, config: JSONConfigStore | None = None):
        self.config = config or JSONConfigStore()

    def is_enabled(self) -> bool:
        return bool(self.config.get("ha_bridge_enabled", False))

    def status(self) -> dict[str, Any]:
        enabled = self.is_enabled()
        return {
            "bridge": "uhome-ha",
            "version": _BRIDGE_VERSION,
            "status": "ok" if enabled else "disabled",
            "enabled": enabled,
            "command_allowlist_size": len(_COMMAND_ALLOWLIST),
        }

    def discover(self) -> dict[str, Any]:
        entities = [
            {
                "id": "uhome.system",
                "type": "service",
                "name": "uHOME System",
                "capabilities": ["info", "capabilities"],
            },
            {
                "id": "uhome.tuner",
                "type": "media_source",
                "name": "uHOME Broadcast Tuner",
                "capabilities": ["discover", "status"],
            },
            {
                "id": "uhome.dvr",
                "type": "recorder",
                "name": "uHOME DVR",
                "capabilities": ["list_rules", "schedule", "cancel"],
            },
            {
                "id": "uhome.ad_processing",
                "type": "processor",
                "name": "uHOME Ad Processing",
                "capabilities": ["get_mode", "set_mode"],
            },
            {
                "id": "uhome.playback",
                "type": "media_player",
                "name": "uHOME Playback",
                "capabilities": ["status", "handoff"],
            },
        ]
        return {
            "bridge": "uhome-ha",
            "version": _BRIDGE_VERSION,
            "entity_count": len(entities),
            "entities": entities,
        }

    def execute_command(self, command: str, params: dict[str, Any]) -> dict[str, Any]:
        if command not in _COMMAND_ALLOWLIST:
            raise ValueError(f"Command not in allowlist: {command!r}")

        if command == "system.info":
            return {"command": "system.info", "result": {"bridge_version": _BRIDGE_VERSION}}
        if command == "system.capabilities":
            return {"command": "system.capabilities", "result": {"allowlist": sorted(_COMMAND_ALLOWLIST)}}
        if command.startswith("uhome."):
            from uhome_server.services.uhome_command_handlers import dispatch

            try:
                return dispatch(command, params)
            except KeyError:
                return {
                    "command": command,
                    "status": "unimplemented",
                    "note": f"Handler for {command!r} not yet wired.",
                    "params": params,
                }
        raise ValueError(f"Unhandled allowlisted command: {command!r}")


def get_ha_service() -> HomeAssistantService:
    return HomeAssistantService()
