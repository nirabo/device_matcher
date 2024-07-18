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
    {
        "test_category": "Alias Key",
        "user_input": ("asset-name", "LAPTOP-2710F80A"),
        "response": {
            "id": 4,
            "name": "LAPTOP-2710F80A",
            "asset_type": "Laptop",
            "model": "20QD00LMUK",
            "ip_address": "192.168.1.4",
            "properties": {
                "kabuto_information": {
                    "os": {
                        "name": "Windows",
                        "last_boot_time": "2021-11-21T09:31:31+01:00",
                        "build": "",
                        "os_architecture": "64-bit",
                        "windows_release_version": "",
                        "pending_reboot": False
                    },
                    "network_adapters": [
                        {
                            "name": "Ethernet 5",
                            "description": "Fortinet SSL VPN Virtual Ethernet Adapter",
                            "type": "ethernet",
                            "ipv4": "169.254.117.211",
                            "ipv6": "fe80::9de0:8da8:cad7:75d3%47",
                            "subnet": "255.255.0.0",
                            "gateway": "",
                            "dns1": "fec0:0:0:ffff::1%1",
                            "dns2": "fec0:0:0:ffff::2%1",
                            "dhcp_server": "",
                            "physical_address": "00-09-0F-AA-00-01",
                            "lease_obtained": "",
                            "lease_expires": "",
                            "dhcp_enabled": True,
                            "autoconfiguration_enabled": True
                        },
                        {
                            "name": "Ethernet",
                            "description": "Intel(R) Ethernet Connection (6) I219-V",
                            "type": "ethernet",
                            "ipv4": "169.254.153.223",
                            "ipv6": "fe80::8c82:6f6e:ec27:99df%8",
                            "subnet": "255.255.0.0",
                            "gateway": "",
                            "dns1": "fec0:0:0:ffff::1%1",
                            "dns2": "fec0:0:0:ffff::2%1",
                            "dhcp_server": "",
                            "physical_address": "F8-75-A4-19-C6-22",
                            "lease_obtained": "",
                            "lease_expires": "",
                            "dhcp_enabled": True,
                            "autoconfiguration_enabled": True
                        },
                        {
                            "name": "Ethernet 2",
                            "description": "TAP-Surfshark Windows Adapter V9",
                            "type": "ethernet",
                            "ipv4": "169.254.189.114",
                            "ipv6": "fe80::a963:a953:3258:bd72%21",
                            "subnet": "255.255.0.0",
                            "gateway": "",
                            "dns1": "fec0:0:0:ffff::1%1",
                            "dns2": "fec0:0:0:ffff::2%1",
                            "dhcp_server": "",
                            "physical_address": "00-FF-82-8B-C6-1F",
                            "lease_obtained": "",
                            "lease_expires": "",
                            "dhcp_enabled": True,
                            "autoconfiguration_enabled": True
                        },
                        {
                            "name": "Local Area Connection* 3",
                            "description": "Microsoft Wi-Fi Direct Virtual Adapter #3",
                            "type": "wifi",
                            "ipv4": "169.254.77.234",
                            "ipv6": "fe80::a935:b8e8:1aaa:4dea%13",
                            "subnet": "255.255.0.0",
                            "gateway": "",
                            "dns1": "fec0:0:0:ffff::1%1",
                            "dns2": "fec0:0:0:ffff::2%1",
                            "dhcp_server": "",
                            "physical_address": "4C-1D-96-46-59-DE",
                            "lease_obtained": "",
                            "lease_expires": "",
                            "dhcp_enabled": True,
                            "autoconfiguration_enabled": True
                        }
                    ]
                }
            }
        }
    }
)

@pytest.mark.parametrize("test_case", USER_INPUTS)
def test_get_asset_from_json(base_url, test_case):
    key, val = test_case["user_input"]
    response = requests.get(f"{base_url}/unstructured_assets/?key={key}&val={val}")
    assert response.status_code == 200
    response_data = response.json()
    assert response_data == test_case["response"]
