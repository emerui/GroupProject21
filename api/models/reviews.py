from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    review = Column(String(1000), nullable=True)
    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"))
    rating = Column(DECIMAL(10,2), nullable=False)
