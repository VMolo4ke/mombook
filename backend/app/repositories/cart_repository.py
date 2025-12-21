from sqlalchemy.orm import Session
from ..models.cart_item import CartItem

class CartRepository:
    def __init__(self, db: Session):
        self.db = db

    # ... существующие методы (get_items_by_session, add_or_update_item) ...
    def get_items_by_session(self, session_id: str):
        return self.db.query(CartItem).filter(
            CartItem.session_id == session_id
        ).order_by(CartItem.id).all()
    
    def add_or_update_item(self, session_id: str, product_id: int, quantity: int):
        # 1. Ищем, есть ли уже такой товар в корзине у этого гостя
        existing_item = self.db.query(CartItem).filter(
            CartItem.session_id == session_id,
            CartItem.product_id == product_id
        ).first()

        if existing_item:
            # 2. Если нашли — увеличиваем количество
            existing_item.quantity += quantity
        else:
            # 3. Если не нашли — создаем новую запись (строку корзины)
            new_item = CartItem(
                session_id=session_id,
                product_id=product_id,
                quantity=quantity
            )
            self.db.add(new_item)
        
        # 4. Сохраняем изменения в базе
        self.db.commit()

    def update_quantity(self, session_id: str, product_id: int, quantity: int):
        """Устанавливает конкретное число товара"""
        item = self.db.query(CartItem).filter(
            CartItem.session_id == session_id,
            CartItem.product_id == product_id
        ).first()
        if item:
            item.quantity = quantity
            self.db.commit()
        return item

    def remove_item(self, session_id: str, product_id: int):
        """Удаляет позицию из корзины"""
        item = self.db.query(CartItem).filter(
            CartItem.session_id == session_id,
            CartItem.product_id == product_id
        ).first()
        if item:
            self.db.delete(item)
            self.db.commit()
        return item

    def clear_all(self, session_id: str):
        """Полностью очищает корзину"""
        self.db.query(CartItem).filter(CartItem.session_id == session_id).delete()
        self.db.commit()
    