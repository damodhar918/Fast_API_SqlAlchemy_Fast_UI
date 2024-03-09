from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date


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
    offer_ends: Optional[date] = None


class DeleteUserForm(BaseModel):
    confirm: bool


class UserForm(BaseModel):
    name: str
    description: Optional[str] = None
    price: int
    is_offer: Optional[bool] = False
    offer_ends: Optional[date] = None


class ItemOut(ItemBase):
    class Config(ConfigDict):
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Item Name",
                "description": "Item Description",
                "price": 100,
                "is_offer": False,
                "offer_ends": date(1993, 1, 1)
            }
        }
        from_attributes = True


# class ItemCreate(ItemBase):
#     pass


# class Item(ItemBase):
#     id: int

#     class Config:
#         from_attributes = True
