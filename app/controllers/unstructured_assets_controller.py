import json

# Define mapping for asset name, model and IP address
NAME_MAP = ("name", "name_snmp", "asset-name")
MODEL_MAP = ("model", "asset-model")
IP_MAP = ("ip_address", "ip-address", "ipv4")

# Global list to hold the assets data
ASSETS = []

def load_assets():
    """
    This function loads the asset data from two separate JSON files and stores it in a global list.
    """
    global ASSETS
    with open("../assets_1.json", 'r') as fid:
        ASSETS_1 = json.load(fid)
    with open("../assets_2.json", 'r') as fid:
        ASSETS_2 = json.load(fid)
    # Append the assets from both files to the global list
    # NOTE: ASSETS_1 contains an object, which holds the list of items, hence we get from it
    ASSETS = [ASSETS_1['assets'], ASSETS_2]

def match_to_mapping(query: str) -> tuple:
    """
    Takes a query string and returns a tuple of mapping keys based on the query.
    If the query is not found in any mapping, an empty tuple is returned.
    """
    result = ()
    if "name" in query:
        return NAME_MAP if query in NAME_MAP else ()
    elif "model" in query:
        return MODEL_MAP if query in MODEL_MAP else ()
    elif "ip" in query:
        return IP_MAP if query in IP_MAP else ()
    return result

def match_obj(obj, mapping, value) -> dict:
    """
    Takes an asset object, a tuple of mapping keys and a value. It checks each key in the mapping
    to see if it exists in the object and if its corresponding value matches the input value. If so, the entire
    object is returned. If no match is found, an empty dictionary is returned.

    TODO: We enforce case ignorance (shall be checked with stakeholders)
    """
    for kmap in mapping:
        if kmap in obj and value.lower() == obj[kmap].lower():
            return obj
    return {}

def filter_assets(qkey: str, qval: str) -> dict:
    """
    Takes a query key and value as input, matches the query key to a mapping, searches each asset in
    the global assets list for a matching object using the mapped keys and input value. If a match is found, the
    matched object is returned. If no match is found, an empty dictionary is returned.
    """
    response = {}
    mapping = match_to_mapping(qkey)
    if not mapping:
        return response
    for asset_set in ASSETS:
        for asset_obj in asset_set:
            response = match_obj(asset_obj, mapping, qval)
            if response:
                return response
    return response
