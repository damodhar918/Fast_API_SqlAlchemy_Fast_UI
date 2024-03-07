from pydantic import BaseModel, ConfigDict
from typing import Optional

# class ItemBase(BaseModel):
#     name: str
#     description: str
#     price: float
#     is_offer: bool


class ItemBase(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: int
    is_offer: Optional[bool] = False


class ItemOut(ItemBase):
    class Config(ConfigDict):
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Item Name",
                "description": "Item Description",
                "price": 100,
                "is_offer": False,
            }
        }
        from_attributes = True

# class ItemCreate(ItemBase):
#     pass


# class Item(ItemBase):
#     id: int

#     class Config:
#         from_attributes = True
