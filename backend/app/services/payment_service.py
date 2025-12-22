import os
from yookassa import Configuration, Payment
from app.config import settings # Импортируем ваши настройки
import uuid

Configuration.configure(settings.yookassa_shop_id, settings.yookassa_secret_key)

class PaymentService:
    def create_yookassa_payment(self, cart, session_id: str):
        payment = Payment.create({
            "amount": {
                "value": "{:.2f}".format(cart.total),
                "currency": "RUB"
            },
            "confirmation": {
                "type": "redirect",
                "return_url": f"{settings.frontend_url}/order-status"
            },
            "capture": True,
            "description": f"Заказ для сессии {session_id}",
            "metadata": {
                "session_id": session_id
            }
        }, str(uuid.uuid4())) # Не забудьте импортировать uuid
        
        return payment