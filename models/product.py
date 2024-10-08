from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

class Product(Base):
    __tablename__ = 'products'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    price: Mapped[float] = mapped_column(db.Float, nullable=False)
    details: Mapped[str] = mapped_column(db.String(300), nullable=True)
    orders: Mapped[List['Order']] = db.relationship(secondary='order_product_association', back_populates='products')