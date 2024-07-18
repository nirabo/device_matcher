from sqlalchemy import Column, Integer, String
from database import Base

class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    ip_address = Column(String, index=True)
    model = Column(String, index=True)
