from typing import Optional
from pydantic import BaseModel


class ResourceBase(BaseModel):
    item: str
    amount: int
    calories: Optional[int] = 0


class ResourceCreate(ResourceBase):
    pass


class ResourceUpdate(BaseModel):
    item: Optional[str] = None
    amount: Optional[int] = None
    calories: Optional[int] = None


class Resource(ResourceBase):
    id: int

    class ConfigDict:
        from_attributes = True
