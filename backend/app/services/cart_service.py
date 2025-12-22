from app.repositories.cart_repository import CartRepository
from app.schemas.cart import CartResponse, CartItemResponse

class CartService:
    def __init__(self, cart_repo: CartRepository):
        self.cart_repo = cart_repo

    def get_full_cart(self, session_id: str) -> CartResponse:
        items_orm = self.cart_repo.get_items_by_session(session_id)
        
        res_items = []
        total_price = 0.0
        total_qty = 0

        for item in items_orm:
            if not item.product:
                continue
                
            line_subtotal = item.product.price * item.quantity
            
            res_items.append(CartItemResponse(
                product_id=item.product_id,
                name=item.product.name,
                price=item.product.price,
                quantity=item.quantity,
                subtotal=line_subtotal,
                image_url=item.product.image_url if hasattr(item.product, 'image_url') else None
            ))
            
            total_price += line_subtotal
            total_qty += item.quantity

        return CartResponse(
            items=res_items,
            total=round(total_price, 2), 
            items_count=total_qty
        )