from fastapi import APIRouter, Depends, Header, HTTPException, Query, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.cart import CartResponse, CartItemCreate
from ..repositories.cart_repository import CartRepository
from ..services.cart_service import CartService


router = APIRouter(prefix="/api/cart", tags=["Cart"])

def get_services(db: Session = Depends(get_db)):
    repo = CartRepository(db)
    return CartService(repo)

@router.get("/", response_model=CartResponse)
def get_cart(x_session_id: str = Header(...), service: CartService = Depends(get_services)):
    return service.get_full_cart(x_session_id)

@router.post("/items", response_model=CartResponse)
def add_item(
    item: CartItemCreate, 
    x_session_id: str = Header(...), 
    service: CartService = Depends(get_services)
):
    service.cart_repo.add_or_update_item(x_session_id, item.product_id, item.quantity)
    return service.get_full_cart(x_session_id)

@router.put("/items/{product_id}", response_model=CartResponse)
def update_item_quantity(
    product_id: int,
    quantity: int = Query(..., gt=0),
    x_session_id: str = Header(...),
    service: CartService = Depends(get_services)
):
    updated = service.cart_repo.update_quantity(x_session_id, product_id, quantity)
    if not updated:
        raise HTTPException(status_code=404, detail="Товар в корзине не найден")
    return service.get_full_cart(x_session_id)

@router.delete("/items/{product_id}", response_model=CartResponse)
def delete_item(
    product_id: int,
    x_session_id: str = Header(...),
    service: CartService = Depends(get_services)
):
    service.cart_repo.remove_item(x_session_id, product_id)
    return service.get_full_cart(x_session_id)

@router.delete("/clear", status_code=204)
def clear_entire_cart(
    x_session_id: str = Header(...),
    db: Session = Depends(get_db)
):
    repo = CartRepository(db)
    repo.clear_cart(x_session_id)
    return None