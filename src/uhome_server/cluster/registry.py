"""File-backed registries for decentralized uHOME nodes and storage volumes."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from uhome_server.config import get_repo_root, read_json_file, utc_now_iso_z, write_json_file


@dataclass
class NodeRecord:
    node_id: str
    hostname: str
    role: str = "server"
    status: str = "online"
    authority: str = "secondary"
    capabilities: list[str] = field(default_factory=list)
    address: str | None = None
    last_seen: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "node_id": self.node_id,
            "hostname": self.hostname,
            "role": self.role,
            "status": self.status,
            "authority": self.authority,
            "capabilities": list(self.capabilities),
            "address": self.address,
            "last_seen": self.last_seen,
            "metadata": dict(self.metadata),
        }


@dataclass
class StorageVolumeRecord:
    volume_id: str
    label: str
    kind: str = "disk"
    status: str = "online"
    mount_path: str | None = None
    node_id: str | None = None
    capacity_bytes: int | None = None
    free_bytes: int | None = None
    tags: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
    last_seen: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "volume_id": self.volume_id,
            "label": self.label,
            "kind": self.kind,
            "status": self.status,
            "mount_path": self.mount_path,
            "node_id": self.node_id,
            "capacity_bytes": self.capacity_bytes,
            "free_bytes": self.free_bytes,
            "tags": list(self.tags),
            "metadata": dict(self.metadata),
            "last_seen": self.last_seen,
        }


class _BaseRegistry:
    key: str

    def __init__(self, repo_root: Path | None = None):
        self.repo_root = repo_root or get_repo_root()
        self.state_path = self.repo_root / "memory" / "uhome" / f"{self.key}.json"

    def _load(self) -> list[dict[str, Any]]:
        payload = read_json_file(self.state_path, default={"items": []})
        items = payload.get("items", [])
        return items if isinstance(items, list) else []

    def _save(self, items: list[dict[str, Any]]) -> None:
        write_json_file(self.state_path, {"updated_at": utc_now_iso_z(), "items": items}, indent=2)


class NodeRegistry(_BaseRegistry):
    key = "nodes"

    def list_nodes(self) -> list[dict[str, Any]]:
        return self._load()

    def upsert_node(self, record: NodeRecord) -> dict[str, Any]:
        items = self._load()
        payload = record.to_dict()
        payload["last_seen"] = payload["last_seen"] or utc_now_iso_z()
        updated = False
        for index, item in enumerate(items):
            if item.get("node_id") == record.node_id:
                items[index] = payload
                updated = True
                break
        if not updated:
            items.append(payload)
        self._save(items)
        return payload

    def mark_node_status(self, node_id: str, status: str) -> dict[str, Any] | None:
        items = self._load()
        for item in items:
            if item.get("node_id") == node_id:
                item["status"] = status
                item["last_seen"] = utc_now_iso_z()
                self._save(items)
                return item
        return None


class StorageRegistry(_BaseRegistry):
    key = "volumes"

    def list_volumes(self) -> list[dict[str, Any]]:
        return self._load()

    def upsert_volume(self, record: StorageVolumeRecord) -> dict[str, Any]:
        items = self._load()
        payload = record.to_dict()
        payload["last_seen"] = payload["last_seen"] or utc_now_iso_z()
        updated = False
        for index, item in enumerate(items):
            if item.get("volume_id") == record.volume_id:
                items[index] = payload
                updated = True
                break
        if not updated:
            items.append(payload)
        self._save(items)
        return payload

    def mark_volume_status(self, volume_id: str, status: str) -> dict[str, Any] | None:
        items = self._load()
        for item in items:
            if item.get("volume_id") == volume_id:
                item["status"] = status
                item["last_seen"] = utc_now_iso_z()
                self._save(items)
                return item
        return None


def get_node_registry(repo_root: Path | None = None) -> NodeRegistry:
    return NodeRegistry(repo_root=repo_root)


def get_storage_registry(repo_root: Path | None = None) -> StorageRegistry:
    return StorageRegistry(repo_root=repo_root)
