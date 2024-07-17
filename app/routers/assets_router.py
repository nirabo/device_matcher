from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from controllers.assets_controller import (
    create_asset,
    get_asset,
    get_assets
)
from schemas.assets_schema import (
    AssetCreateSchema,
    AssetSchema
)

from database import get_db

assets_router = APIRouter()

@assets_router.post("/assets/", response_model=AssetSchema)
def create_asset_route(asset: AssetCreateSchema, db: Session = Depends(get_db)):
    return create_asset(db, asset)

@assets_router.get("/assets/{asset_id}", response_model=AssetSchema)
def read_asset_route(asset_id: int, db: Session = Depends(get_db)):
    db_asset = get_asset(db, asset_id)
    if db_asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")
    return db_asset

@assets_router.get("/assets/", response_model=list[AssetSchema])
def read_assets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    drivers = get_assets(db, skip=skip, limit=limit)
    return drivers