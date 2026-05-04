from sqlalchemy import Column, Integer, String, DECIMAL
from sqlalchemy.orm import relationship

from ..dependencies.database import Base


class Sandwich(Base):
    __tablename__ = "sandwiches"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sandwich_name = Column(String(100), unique=True, nullable=False)
    price = Column(DECIMAL(6, 2), nullable=False, server_default="0.00")
    category = Column(String(50), nullable=True)
    description = Column(String(500), nullable=True)

    recipes = relationship("Recipe", back_populates="sandwich")
    order_details = relationship("OrderDetail", back_populates="sandwich")