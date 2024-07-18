# assets_routers.py
from fastapi import APIRouter, HTTPException
from controllers.unstructured_assets_controller import filter_assets, load_assets

router = APIRouter()

@router.get("/unstructured_assets/")
async def get_asset_from_json(key: str, val: str):
    load_assets()
    asset = filter_assets(key, val)
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    return asset
