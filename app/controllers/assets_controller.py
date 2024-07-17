from sqlalchemy.orm import Session

from models.assets_models import AssetModel
from schemas.assets_schema import AssetSchema

from database import get_db

def create_asset(db: Session, asset: AssetSchema):
    db_asset = AssetModel(**asset.model_dump())
    db.add(db_asset)
    db.commit()
    db.refresh(db_asset)
    return db_asset

def get_assets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(AssetModel).offset(skip).limit(limit).all()

def get_asset(db: Session, asset_id: int):
    return db.query(AssetModel).filter(AssetModel.id == asset_id)