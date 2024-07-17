from pydantic import BaseModel, Field, AliasChoices


class AssetBaseSchema(BaseModel):
    """
    Schema for temporary or used for transient purposes.
    """

    name: str = Field(
        validation_alias=AliasChoices(
            "name",
            "asset_name"
        )
    )
    ip_address: str = Field(
        validation_alias=AliasChoices(
            'ip-address', 
            'ipv4',
        )
    )
    model: str = Field(
        validation_alias=AliasChoices(
            "model",
            "asset-model"
        )
    )

class AssetCreateSchema(AssetBaseSchema): 
    """
    Schema intended for assets to be saved to a database or stored persistently
    """
    pass


class AssetSchema(AssetCreateSchema):
    id: int
    class Config:
        from_attributes = True