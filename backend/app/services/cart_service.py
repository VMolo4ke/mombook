from app.repositories.cart_repository import CartRepository
from app.schemas.cart import CartResponse, CartItemResponse

class CartService:
    def __init__(self, cart_repo: CartRepository):
        self.cart_repo = cart_repo

    def get_full_cart(self, session_id: str) -> CartResponse:
        # 1. Получаем список товаров из репозитория (уже синхронно)
        items_orm = self.cart_repo.get_items_by_session(session_id)
        
        res_items = []
        total_price = 0.0
        total_qty = 0

        # 2. Проходим по каждой позиции и готовим данные для ответа
        for item in items_orm:
            # item.product доступен благодаря relationship в модели
            if not item.product:
                continue
                
            # Расчет стоимости позиции (количество * цена за 1 шт)
            line_subtotal = item.product.price * item.quantity
            
            # Создаем объект по схеме CartItemResponse
            res_items.append(CartItemResponse(
                product_id=item.product_id,
                name=item.product.name,
                price=item.product.price,
                quantity=item.quantity,
                subtotal=line_subtotal,
                image_url=item.product.image_url if hasattr(item.product, 'image_url') else None
            ))
            
            # Накапливаем общие итоги
            total_price += line_subtotal
            total_qty += item.quantity

        # 3. Формируем финальный ответ по схеме CartResponse
        return CartResponse(
            items=res_items,
            total=round(total_price, 2), # Округляем до копеек
            items_count=total_qty
        )