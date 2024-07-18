# assets_routers.py
from fastapi import APIRouter, HTTPException
from controllers.unstructured_assets_controller import filter_assets, load_assets, normalize_asset, match_obj_by_val

router = APIRouter()

@router.get("/unstructured_assets/")
async def get_asset_from_json(key: str, val: str):
    assets = load_assets()
    asset = filter_assets(assets, key, val)
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    return asset

@router.get("/unstructured_assets/normalized/")
async def get_normalized_assets():
    assets = load_assets()
    normalized_assets = []
    for asset_set in assets:
        for asset in asset_set:
            normalized_assets.append(normalize_asset(asset.copy()))
    return normalized_assets

@router.get("/unstructured_assets/by_value/")
async def get_unstructured_by_value(query: str):
    assets = load_assets()
    normalized_asset = []
    for asset_set in assets:
        for asset in asset_set:
            response = match_obj_by_val(asset, query)
            if response:
                normalized_asset.append(response.copy())
                break
        if normalized_asset:
            break
    if not normalized_asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    return normalized_asset