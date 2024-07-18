# tests/test_main.py
import pytest
import requests
import json

@pytest.fixture
def base_url():
    return "http://localhost:8123"

USER_INPUTS = (
    {
        "test_category": "Alias Key",
        "user_input": ("ipv4", "192.168.77.2"),
        "response": {
            "id": 11,
            "asset-name": "Another Test Device",
            "asset-model": "Some model",
            "mac-address": "AA:BB:CC:DD:EE:02",
            "ip-address": "192.168.77.2"
        }
    },
    {
        "test_category": "Real Key",
        "user_input": ("asset-name", "Netgear Access Point"),
        "response": {
            "id": 16,
            "asset-name": "Netgear Access Point",
            "asset-model": "WAX620",
            "mac-address": "AA:BB:CC:DD:EE:07",
            "ip-address": "192.168.77.7"
        },       
    },
    {
        "test_category": "Alias Key",
        "user_input": ("name", "Netgear Access Point"),
        "response": {
            "id": 16,
            "asset-name": "Netgear Access Point",
            "asset-model": "WAX620",
            "mac-address": "AA:BB:CC:DD:EE:07",
            "ip-address": "192.168.77.7"
        },       
    },
    {
        "test_category": "Real Key",
        "user_input": ("ip-address", "192.168.77.7"),
        "response": {
            "id": 16,
            "asset-name": "Netgear Access Point",
            "asset-model": "WAX620",
            "mac-address": "AA:BB:CC:DD:EE:07",
            "ip-address": "192.168.77.7"
        },       
    },
    {
        "test_category": "Alias Key",
        "user_input": ("ip_address", "192.168.77.7"),
        "response": {
            "id": 16,
            "asset-name": "Netgear Access Point",
            "asset-model": "WAX620",
            "mac-address": "AA:BB:CC:DD:EE:07",
            "ip-address": "192.168.77.7"
        },       
    },
    {
        "test_category": "Alias Key",
        "user_input": ("ipv4", "192.168.77.7"),
        "response": {
            "id": 16,
            "asset-name": "Netgear Access Point",
            "asset-model": "WAX620",
            "mac-address": "AA:BB:CC:DD:EE:07",
            "ip-address": "192.168.77.7"
        },       
    },
    {
        "test_category": "Alias Key",
        "user_input": ("name", "Another Test Device"),
        "response": {
            "id": 11,
            "asset-name": "Another Test Device",
            "asset-model": "Some model",
            "mac-address": "AA:BB:CC:DD:EE:02",
            "ip-address": "192.168.77.2"
        },     
    },
)

@pytest.mark.parametrize("test_case", USER_INPUTS)
def test_get_asset_from_json(base_url, test_case):
    key, val = test_case["user_input"]
    response = requests.get(f"{base_url}/unstructured_assets/?key={key}&val={val}")
    assert response.status_code == 200
    response_data = response.json()
    assert response_data == test_case["response"]
