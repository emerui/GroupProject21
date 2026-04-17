from typing import Optional
from pydantic import BaseModel


class PaymentBase(BaseModel):
    order_id: int
    payment_type: str  # 'card' or 'cash'


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(BaseModel):
    payment_type: Optional[str] = None


class Payment(PaymentBase):
    id: int

    class ConfigDict:
        from_attributes = True
