from fastapi import APIRouter, Depends, Header, Request, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.cart_service import CartService
from app.services.payment_service import PaymentService
from app.repositories.cart_repository import CartRepository
from app.models.order import Order
from app.repositories.payment_repository import PaymentRepository


class PaymentCreateResponse(BaseModel):
    email: str
    tel: str
    address: str


router = APIRouter(prefix="/payments", tags=["Payments"])

@router.post("/create")
def create_payment(
    data: PaymentCreateResponse,
    x_session_id: str = Header(...),
    db: Session = Depends(get_db)
):
    cart_service = CartService(CartRepository(db))
    cart = cart_service.get_full_cart(x_session_id)
    
    if not cart.items:
        raise HTTPException(status_code=400, detail="Cart is empty")

    pay_service = PaymentService()
    payment = pay_service.create_yookassa_payment(cart, x_session_id)

    # Формируем список товаров для сохранения
    cart_items_data = [
        {
            "product_id": item.product_id,
            "name": item.name,
            "quantity": item.quantity,
            "price": item.price,
            "image_url": item.image_url
        } for item in cart.items
    ]

    pay_repo = PaymentRepository(db)
    pay_repo.create_order(
        session_id=x_session_id, 
        total=cart.total, 
        payment_id=payment.id,
        email=data.email,
        tel=data.tel,
        address=data.address,
        items_json=cart_items_data
    )

    
    return {
        "confirmation_url": payment.confirmation.confirmation_url,
        "payment_id": payment.id
    }

@router.post("/webhook")
async def yookassa_webhook(request: Request, db: Session = Depends(get_db)):
    data = await request.json()
    
    if data.get("event") == "payment.succeeded":
        payment_obj = data.get("object")
        payment_id = payment_obj.get("id") # ID платежа в ЮKassa
        session_id = payment_obj.get("metadata", {}).get("session_id")
        
        if session_id:
            # 1. Очищаем корзину
            cart_repo = CartRepository(db)
            cart_repo.clear_all(session_id) 
            
            # 2. !!! ОБЯЗАТЕЛЬНО: Обновляем статус заказа !!!
            order = db.query(Order).filter(Order.yookassa_payment_id == payment_id).first()
            if order:
                order.status = 'paid'
                db.commit()
            
            print(f"Заказ {payment_id} оплачен, корзина {session_id} очищена")
            
    return {"status": "ok"}

@router.get("/last-status")
def get_last_order_status(
    x_session_id: str = Header(...),
    db: Session = Depends(get_db)
):
    order = db.query(Order).filter(Order.session_id == x_session_id).order_by(Order.id.desc()).first()
    if not order:
        return {"status": "not_found"}
    return {"status": order.status}