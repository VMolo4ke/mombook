from pydantic import BaseModel

class PaymentCreateResponse(BaseModel):
    confirmation_url: str
    payment_id: str
    email: str
    tel: str
    address: str

class WebhookData(BaseModel):
    event: str
    object: dict