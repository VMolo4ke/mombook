from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from ..models.order import Order

router = APIRouter()

@router.get("/orders")
def get_all_orders(db: Session = Depends(get_db)):
    orders = db.query(Order).all()
    return orders