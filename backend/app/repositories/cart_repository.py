from sqlalchemy.orm import Session
from ..models.cart_item import CartItem

class CartRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_items_by_session(self, session_id: str):
        return self.db.query(CartItem).filter(
            CartItem.session_id == session_id
        ).order_by(CartItem.id).all()
    
    def add_or_update_item(self, session_id: str, product_id: int, quantity: int):
        existing_item = self.db.query(CartItem).filter(
            CartItem.session_id == session_id,
            CartItem.product_id == product_id
        ).first()

        if existing_item:
            existing_item.quantity += quantity
        else:
            new_item = CartItem(
                session_id=session_id,
                product_id=product_id,
                quantity=quantity
            )
            self.db.add(new_item)
        
        self.db.commit()

    def update_quantity(self, session_id: str, product_id: int, quantity: int):
        item = self.db.query(CartItem).filter(
            CartItem.session_id == session_id,
            CartItem.product_id == product_id
        ).first()
        if item:
            item.quantity = quantity
            self.db.commit()
        return item

    def remove_item(self, session_id: str, product_id: int):
        item = self.db.query(CartItem).filter(
            CartItem.session_id == session_id,
            CartItem.product_id == product_id
        ).first()
        if item:
            self.db.delete(item)
            self.db.commit()
        return item

    def clear_all(self, session_id: str):
        self.db.query(CartItem).filter(CartItem.session_id == session_id).delete()
        self.db.commit()
    