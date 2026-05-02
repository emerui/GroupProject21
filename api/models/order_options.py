from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class OrderOption(Base):
    __tablename__ = "order_options"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_detail_id = Column(Integer, ForeignKey("order_details.id"), nullable=False)
    option_name = Column(String(100), nullable=False)
    option_value = Column(String(100), nullable=False)
    order_detail = relationship("OrderDetail", back_populates="order_options")