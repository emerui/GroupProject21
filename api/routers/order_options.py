from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from ..controllers import order_options as controller
from ..schemas import order_options as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Order Options'],
    prefix="/order_options"
)

@router.post("/", response_model=schema.OrderOption)
def create(request: schema.OrderOptionCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.OrderOption])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{item_id}", response_model=schema.OrderOption)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)

@router.put("/{item_id}", response_model=schema.OrderOption)
def update(item_id: int, request: schema.OrderOptionUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)

@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)