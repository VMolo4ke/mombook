from sqlalchemy.orm import Session
from app.models.order import Order
from app.models.cart_item import CartItem

class PaymentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_order(self, session_id: str, total: float, payment_id: str, email: str, tel: str, address: str, items_json):
        new_order = Order(
            session_id=session_id,
            total_amount=total,
            yookassa_payment_id=payment_id,
            email=email,
            tel=tel,
            address=address,
            items=items_json,
            status='pending'
        )
        self.db.add(new_order)
        self.db.commit()
        self.db.refresh(new_order)
        return new_order

    def confirm_payment(self, payment_id: str):
        order = self.db.query(Order).filter(Order.yookassa_payment_id == payment_id).first()
        if order:
            order.status = 'paid'
            self.db.commit()
            return order.session_id
        return None