from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ReviewBase(BaseModel):
    review: str
    sandwich_id: int


class ReviewCreate(ReviewBase):
    pass


class ReviewUpdate(BaseModel):
    review: Optional[str] = None
    sandwich_id: Optional[int] = None


class Review(ReviewBase):
    id: int

    class ConfigDict:
        from_attributes = True