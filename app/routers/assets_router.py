from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from controllers.assets_controller import get_asset, get_assets, create_asset, update_asset, delete_asset
from schemas.assets_schema import AssetCreateSchema, AssetSchema
from database import get_db

router = APIRouter()

@router.post("/assets/", response_model=AssetSchema)
def create_asset_route(asset: AssetCreateSchema, db: Session = Depends(get_db)):
    return create_asset(db=db, asset=asset)

@router.get("/assets/", response_model=list[AssetSchema])
def read_assets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    assets = get_assets(db, skip=skip, limit=limit)
    return assets

@router.get("/assets/{asset_id}", response_model=AssetSchema)
def read_asset(asset_id: int, db: Session = Depends(get_db)):
    db_asset = get_asset(db, asset_id=asset_id)
    if db_asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")
    return db_asset

@router.put("/assets/{asset_id}", response_model=AssetSchema)
def update_asset_route(asset_id: int, asset: AssetCreateSchema, db: Session = Depends(get_db)):
    return update_asset(db=db, asset_id=asset_id, asset=asset)

@router.delete("/assets/{asset_id}")
def delete_asset_route(asset_id: int, db: Session = Depends(get_db)):
    return delete_asset(db=db, asset_id=asset_id)
