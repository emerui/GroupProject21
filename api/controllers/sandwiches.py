from sqlalchemy.orm import Session
from sqlalchemy import or_

from api.models.sandwiches import Sandwich
from api.schemas.sandwiches import SandwichCreate, SandwichUpdate


def create(db: Session, request: SandwichCreate):
    new_sandwich = Sandwich(
        sandwich_name=request.sandwich_name,
        price=request.price,
        category=request.category,
        description=request.description,
    )

    db.add(new_sandwich)
    db.commit()
    db.refresh(new_sandwich)

    return new_sandwich


def read_all(db: Session):
    return db.query(Sandwich).all()


def read_one(db: Session, sandwich_id: int):
    return db.query(Sandwich).filter(Sandwich.id == sandwich_id).first()


def update(db: Session, sandwich_id: int, request: SandwichUpdate):
    sandwich = db.query(Sandwich).filter(Sandwich.id == sandwich_id).first()

    if sandwich is None:
        return None

    update_data = request.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(sandwich, key, value)

    db.commit()
    db.refresh(sandwich)

    return sandwich


def delete(db: Session, sandwich_id: int):
    sandwich = db.query(Sandwich).filter(Sandwich.id == sandwich_id).first()

    if sandwich is None:
        return None

    db.delete(sandwich)
    db.commit()

    return sandwich


def search(db: Session, search_term: str):
    return (
        db.query(Sandwich)
        .filter(
            or_(
                Sandwich.sandwich_name.ilike(f"%{search_term}%"),
                Sandwich.category.ilike(f"%{search_term}%"),
                Sandwich.description.ilike(f"%{search_term}%"),
            )
        )
        .all()
    )