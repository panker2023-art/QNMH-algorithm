import pytest
from fastapi.testclient import TestClient
from src.main import app
import os
import networkx as nx
import asyncio
import uuid

client = TestClient(app)

@pytest.fixture
def dummy_networks(tmp_path):
    # Create two dummy edgelist files for testing
    src_file = tmp_path / "src_net.txt"
    ref_file = tmp_path / "ref_net.txt"
    
    G1 = nx.Graph()
    G1.add_edges_from([('A', 'B'), ('B', 'C')])
    nx.write_edgelist(G1, src_file, data=False)
    
    G2 = nx.Graph()
    G2.add_edges_from([('X', 'Y'), ('Y', 'Z')])
    nx.write_edgelist(G2, ref_file, data=False)
    
    return str(src_file), str(ref_file)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "version": "0.1.0"}

def test_qnmh_workflow(dummy_networks):
    src_path, ref_path = dummy_networks
    
    # Submit task
    payload = {
        "matrix_file_path": src_path,
        "reference_network_path": ref_path,
        "metadata": {"genetic_robustness": 0.9}
    }
    
    response = client.post("/analysis/qnmh", json=payload)
    assert response.status_code == 202
    data = response.json()
    assert "task_id" in data
    
    task_id = data["task_id"]
    
    # Normally we would poll here with asyncio.sleep in a real client,
    # but since TestClient is synchronous and blocks the event loop differently, 
    # we just check the initial PENDING/RUNNING state to ensure the endpoint works.
    
    poll_response = client.get(f"/analysis/qnmh/{task_id}")
    assert poll_response.status_code == 200
    poll_data = poll_response.json()
    assert poll_data["task_id"] == task_id
    assert poll_data["status"] in ["PENDING", "RUNNING", "COMPLETED"]
