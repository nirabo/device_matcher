# assets_routers.py
from fastapi import APIRouter, HTTPException
from controllers.unstructured_assets_controller import filter_assets, load_assets, normalize_asset

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
            normalized_assets.append(normalize_asset(asset))
    return normalized_assets