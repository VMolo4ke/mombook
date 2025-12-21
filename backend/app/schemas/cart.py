from pydantic import BaseModel, Field
from typing import Optional

class CartItemCreate(BaseModel):
    product_id: int
    quantity: int = Field(..., gt=0)

class CartItemResponse(BaseModel):
    product_id: int
    name: str
    price: float
    quantity: int
    subtotal: float
    image_url: Optional[str] = None

class CartResponse(BaseModel):
    items: list[CartItemResponse]
    total: float
    items_count: int