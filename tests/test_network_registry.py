from fastapi import FastAPI
from fastapi.testclient import TestClient

from uhome_server.routes import network as network_routes


def _client(monkeypatch):
    node_store = {}
    volume_store = {}

    class _Nodes:
        def list_nodes(self):
            return list(node_store.values())

        def upsert_node(self, record):
            payload = record.to_dict()
            node_store[payload["node_id"]] = payload
            return payload

        def mark_node_status(self, node_id, status):
            item = node_store.get(node_id)
            if item is None:
                return None
            item["status"] = status
            return item

    class _Volumes:
        def list_volumes(self):
            return list(volume_store.values())

        def upsert_volume(self, record):
            payload = record.to_dict()
            volume_store[payload["volume_id"]] = payload
            return payload

        def mark_volume_status(self, volume_id, status):
            item = volume_store.get(volume_id)
            if item is None:
                return None
            item["status"] = status
            return item

    monkeypatch.setattr(network_routes, "get_node_registry", lambda: _Nodes())
    monkeypatch.setattr(network_routes, "get_storage_registry", lambda: _Volumes())
    app = FastAPI()
    app.include_router(network_routes.router)
    return TestClient(app)


def test_upsert_and_list_nodes(monkeypatch):
    client = _client(monkeypatch)
    response = client.post(
        "/api/network/nodes",
        json={
            "node_id": "node-a",
            "hostname": "uhome-a.local",
            "authority": "primary",
            "capabilities": ["ingest", "playback"],
        },
    )
    assert response.status_code == 200
    listed = client.get("/api/network/nodes")
    assert listed.status_code == 200
    body = listed.json()
    assert body["count"] == 1
    assert body["nodes"][0]["node_id"] == "node-a"


def test_update_node_status(monkeypatch):
    client = _client(monkeypatch)
    client.post("/api/network/nodes", json={"node_id": "node-a", "hostname": "uhome-a.local"})
    response = client.post("/api/network/nodes/node-a/status", json={"status": "offline"})
    assert response.status_code == 200
    assert response.json()["node"]["status"] == "offline"


def test_upsert_and_list_volumes(monkeypatch):
    client = _client(monkeypatch)
    response = client.post(
        "/api/network/volumes",
        json={
            "volume_id": "vol-1",
            "label": "Media Array A",
            "kind": "partition",
            "node_id": "node-a",
            "mount_path": "/srv/media-a",
            "tags": ["movies", "archive"],
        },
    )
    assert response.status_code == 200
    listed = client.get("/api/network/volumes")
    assert listed.status_code == 200
    body = listed.json()
    assert body["count"] == 1
    assert body["volumes"][0]["volume_id"] == "vol-1"


def test_update_volume_status_404(monkeypatch):
    client = _client(monkeypatch)
    response = client.post("/api/network/volumes/missing/status", json={"status": "offline"})
    assert response.status_code == 404
