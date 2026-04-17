from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100), nullable=False)
    phone = Column(String(20), nullable=True)
    address = Column(String(200), nullable=True)

    orders = relationship("Order", back_populates="customer")
