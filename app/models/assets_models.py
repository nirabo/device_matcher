from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.sqlite import JSON

from database import Base

class AssetModel(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)
    ip_address = Column(JSON)
    name = Column(String)
    model = Column(String)