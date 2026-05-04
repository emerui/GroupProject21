from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from api.controllers import sandwiches as controller
from api.dependencies.database import get_db
from api.schemas.sandwiches import Sandwich, SandwichCreate, SandwichUpdate


router = APIRouter(
    prefix="/sandwiches",
    tags=["Sandwiches"],
)


@router.post("/", response_model=Sandwich, status_code=status.HTTP_201_CREATED)
def create_sandwich(request: SandwichCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=List[Sandwich])
def get_all_sandwiches(db: Session = Depends(get_db)):
    return controller.read_all(db=db)


@router.get("/search", response_model=List[Sandwich])
def search_sandwiches(search_term: str, db: Session = Depends(get_db)):
    return controller.search(db=db, search_term=search_term)


@router.get("/{sandwich_id}", response_model=Sandwich)
def get_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    sandwich = controller.read_one(db=db, sandwich_id=sandwich_id)

    if sandwich is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sandwich not found",
        )

    return sandwich


@router.put("/{sandwich_id}", response_model=Sandwich)
def update_sandwich(
    sandwich_id: int,
    request: SandwichUpdate,
    db: Session = Depends(get_db),
):
    sandwich = controller.update(
        db=db,
        sandwich_id=sandwich_id,
        request=request,
    )

    if sandwich is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sandwich not found",
        )

    return sandwich


@router.delete("/{sandwich_id}", response_model=Sandwich)
def delete_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    sandwich = controller.delete(db=db, sandwich_id=sandwich_id)

    if sandwich is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sandwich not found",
        )

    return sandwich