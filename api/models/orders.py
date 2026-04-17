from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100))
    order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    description = Column(String(300))
    phone = Column(String(20), nullable=True)
    address = Column(String(200), nullable=True)
    order_type = Column(String(10), nullable=False, server_default='dine_in')  # 'dine_in' or 'takeout'
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=True)
    promo_id = Column(Integer, ForeignKey("promotions.id"), nullable=True)

    order_details = relationship("OrderDetail", back_populates="order")
    customer = relationship("Customer", back_populates="orders")
    promotion = relationship("Promotion", back_populates="orders")
    payment = relationship("Payment", back_populates="order", uselist=False)