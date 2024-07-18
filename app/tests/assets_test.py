import pytest
import requests
import json

@pytest.fixture
def base_url():
    return "http://localhost:8123"

def test_create_asset(base_url):
    data = {
        "name": "Test Asset",
        "ip_address": "192.168.0.1",
        "model": "Test Model"
    }
    response = requests.post(f"{base_url}/assets/", json=data)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["name"] == data["name"]
    assert response_data["ip_address"] == data["ip_address"]
    assert response_data["model"] == data["model"]
    assert "id" in response_data
    asset_id = response_data["id"]

    response = requests.get(f"{base_url}/assets/{asset_id}")
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["name"] == data["name"]
    assert response_data["ip_address"] == data["ip_address"]
    assert response_data["model"] == data["model"]
    assert response_data["id"] == asset_id

    updated_data = {
        "name": "Updated Asset",
        "ip_address": "192.168.0.2",
        "model": "Updated Model"
    }
    response = requests.put(f"{base_url}/assets/{asset_id}", json=updated_data)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["name"] == updated_data["name"]
    assert response_data["ip_address"] == updated_data["ip_address"]
    assert response_data["model"] == updated_data["model"]
    assert response_data["id"] == asset_id

    response = requests.delete(f"{base_url}/assets/{asset_id}")
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["ok"] == True

    response = requests.get(f"{base_url}/assets/{asset_id}")
    assert response.status_code == 404
    response_data = response.json()
    assert response_data["detail"] == "Asset not found"
