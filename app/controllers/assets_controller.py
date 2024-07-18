from sqlalchemy.orm import Session
from models.assets_models import Asset
from schemas.assets_schema import AssetCreateSchema, AssetSchema
from fastapi import HTTPException

def get_asset(db: Session, asset_id: int):
    return db.query(Asset).filter(Asset.id == asset_id).first()

def get_assets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Asset).offset(skip).limit(limit).all()

def create_asset(db: Session, asset: AssetCreateSchema):
    db_asset = Asset(name=asset.name, ip_address=asset.ip_address, model=asset.model)
    db.add(db_asset)
    db.commit()
    db.refresh(db_asset)
    return db_asset

def update_asset(db: Session, asset_id: int, asset: AssetCreateSchema):
    db_asset = db.query(Asset).filter(Asset.id == asset_id).first()
    if not db_asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    db_asset.name = asset.name
    db_asset.ip_address = asset.ip_address
    db_asset.model = asset.model
    db.commit()
    db.refresh(db_asset)
    return db_asset

def delete_asset(db: Session, asset_id: int):
    db_asset = db.query(Asset).filter(Asset.id == asset_id).first()
    if not db_asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    db.delete(db_asset)
    db.commit()
    return {"ok": True}
