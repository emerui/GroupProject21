from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import orders as model
from ..models.customers import Customer
from sqlalchemy.exc import SQLAlchemyError
from datetime import date


def create(db: Session, request):
    try:
        customer = None

        if request.customer_id:
            customer = db.query(Customer).filter(Customer.id == request.customer_id).first()
            if not customer:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID Customer not found!")
        if not request.customer_id and not request.customer_name:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer name needed")
        new_item = model.Order(
            customer_id = request.customer_id,
            customer_name= customer.customer_name if customer else request.customer_name,
            phone = customer.phone if customer else request.phone,
            address = customer.address if customer else request.address,
            description=request.description,
            order_type = request.order_type,
            promo_id = request.promo_id
        )
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item


def read_all(db: Session):
    try:
        result = db.query(model.Order).all()
        for item in result:
            item.total_price = calculate_order_total(item)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, item_id):
    try:
        item = db.query(model.Order).filter(model.Order.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.total_price = calculate_order_total(item)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def update(db: Session, item_id, request):
    try:
        item = db.query(model.Order).filter(model.Order.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()


def delete(db: Session, item_id):
    try:
        item = db.query(model.Order).filter(model.Order.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

def calculate_order_total(order):
    total = 0

    for item in order.order_details:
        total += item.sandwich.price * item.amount

    if order.promotion:
        if order.promotion.expiration_date>= date.today():
            total -= total * (order.promotion.discount / 100)

    return round(float(total), 2)
