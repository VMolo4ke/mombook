from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from ..database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    description = Column(Text, nullable=False)
    price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    image_url = Column(String)
    createdAt = Column(DateTime, default=datetime.now(timezone.utc))

    category = relationship("Category", back_populates="products")
    cart_items = relationship("CartItem", back_populates="product")

    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.name}', price={self.price})>"
    