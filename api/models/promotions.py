from sqlalchemy import Column, Integer, String, DECIMAL, DATE
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Promotion(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)
    discount = Column(DECIMAL(5, 2), nullable=False, server_default='0.0')
    min_order_amount = Column(DECIMAL(6, 2), nullable=True, server_default='0.0')
    expiration_date = Column(DATE, nullable=True)

    orders = relationship("Order", back_populates="promotion")
