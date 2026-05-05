from fastapi import APIRouter, Depends, FastAPI, status, Response, Query
from sqlalchemy.orm import Session
from ..controllers import orders as controller
from ..schemas import orders as schema
from ..dependencies.database import engine, get_db
from datetime import date


router = APIRouter(
    tags=['Orders'],
    prefix="/orders"
)


@router.post("/", response_model=schema.Order)
def create(request: schema.OrderCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/range", response_model = list[schema.Order])
def get_range(
        start_date: date = Query(),
        end_date: date = Query(),
        db: Session = Depends(get_db)
):
    return controller.date_range(db, start_date, end_date)


@router.get("/", response_model=list[schema.Order])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{item_id}", response_model=schema.Order)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)

@router.get("/history/{customer_id}", response_model=list[schema.Order])
def order_history(customer_id: int, db: Session = Depends(get_db)):
    return controller.order_history(db, customer_id=customer_id)


@router.put("/{item_id}", response_model=schema.Order)
def update(item_id: int, request: schema.OrderUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)


@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)

@router.get("/revenue/daily")
def get_revenue(target_date: date, db: Session = Depends(get_db)):
    return controller.total_revenue(db, target_date)

