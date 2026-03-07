"""Network and storage routes for decentralized uHOME server topologies."""

from __future__ import annotations

from typing import Any
from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from uhome_server.cluster.registry import (
    NodeRecord,
    StorageVolumeRecord,
    get_node_registry,
    get_storage_registry,
)

router = APIRouter(prefix="/api/network", tags=["network"])


class NodeUpsertRequest(BaseModel):
    node_id: str
    hostname: str
    role: str = "server"
    status: str = "online"
    authority: str = "secondary"
    capabilities: list[str] = Field(default_factory=list)
    address: Optional[str] = None
    metadata: dict[str, Any] = Field(default_factory=dict)


class StatusUpdateRequest(BaseModel):
    status: str


class VolumeUpsertRequest(BaseModel):
    volume_id: str
    label: str
    kind: str = "disk"
    status: str = "online"
    mount_path: Optional[str] = None
    node_id: Optional[str] = None
    capacity_bytes: Optional[int] = None
    free_bytes: Optional[int] = None
    tags: list[str] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)


@router.get("/nodes")
async def list_nodes():
    nodes = get_node_registry().list_nodes()
    return {"count": len(nodes), "nodes": nodes}


@router.post("/nodes")
async def upsert_node(payload: NodeUpsertRequest):
    record = NodeRecord(**payload.model_dump())
    node = get_node_registry().upsert_node(record)
    return {"success": True, "node": node}


@router.post("/nodes/{node_id}/status")
async def update_node_status(node_id: str, payload: StatusUpdateRequest):
    node = get_node_registry().mark_node_status(node_id, payload.status)
    if node is None:
        raise HTTPException(status_code=404, detail=f"Node not found: {node_id}")
    return {"success": True, "node": node}


@router.get("/volumes")
async def list_volumes():
    volumes = get_storage_registry().list_volumes()
    return {"count": len(volumes), "volumes": volumes}


@router.post("/volumes")
async def upsert_volume(payload: VolumeUpsertRequest):
    record = StorageVolumeRecord(**payload.model_dump())
    volume = get_storage_registry().upsert_volume(record)
    return {"success": True, "volume": volume}


@router.post("/volumes/{volume_id}/status")
async def update_volume_status(volume_id: str, payload: StatusUpdateRequest):
    volume = get_storage_registry().mark_volume_status(volume_id, payload.status)
    if volume is None:
        raise HTTPException(status_code=404, detail=f"Volume not found: {volume_id}")
    return {"success": True, "volume": volume}
