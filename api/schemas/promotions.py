from datetime import date
from typing import Optional
from pydantic import BaseModel


class PromotionBase(BaseModel):
    name: str
    discount: float
    expiration_date: Optional[date] = None


class PromotionCreate(PromotionBase):
    pass


class PromotionUpdate(BaseModel):
    name: Optional[str] = None
    discount: Optional[float] = None
    expiration_date: Optional[date] = None


class Promotion(PromotionBase):
    id: int

    class ConfigDict:
        from_attributes = True
