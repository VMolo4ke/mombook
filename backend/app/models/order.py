from sqlalchemy import JSON, Column, Integer, String, Float, DateTime, Enum
from app.database import Base
import datetime

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String, nullable=False)
    total_amount = Column(Float, nullable=False)
    yookassa_payment_id = Column(String, index=True, nullable=False)
    email = Column(String, nullable=False)
    tel = Column(String, nullable=False)
    address = Column(String, nullable=False)
    items = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.now)
    
    status = Column(Enum('pending', 'paid', 'failed', name='order_status'), default='pending')