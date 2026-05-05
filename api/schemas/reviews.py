from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class ReviewBase(BaseModel):
    review: str
    sandwich_id: int
    rating: float = Field(ge=1, le=5)


class ReviewCreate(ReviewBase):
    pass


class ReviewUpdate(BaseModel):
    review: Optional[str] = None
    sandwich_id: Optional[int] = None
    rating: Optional[float] = None


class Review(ReviewBase):
    id: int

    class Config:
        from_attributes = True