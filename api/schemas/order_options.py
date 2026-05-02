from typing import Optional
from pydantic import BaseModel

class OrderOptionBase(BaseModel):
    order_detail_id: int
    option_name: str
    option_value: str

class OrderOptionCreate(OrderOptionBase):
    pass

class OrderOptionUpdate(BaseModel):
    order_detail_id: Optional[int] = None
    option_name: Optional[str] = None
    option_value: Optional[str] = None

class OrderOption(OrderOptionBase):
    id: int
    class ConfigDict:
        from_attributes = True