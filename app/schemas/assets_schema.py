from pydantic import BaseModel


class AssetBaseSchema(BaseModel):
    """
    Schema for temporary or used for transient purposes.
    """
    name: str
    ip_address: str
    model: str

class AssetCreateSchema(AssetBaseSchema): 
    """
    Schema intended for assets to be saved to a database or stored persistently
    """
    pass


class AssetSchema(AssetCreateSchema):
    id: int
    class Config:
        from_attributes = True