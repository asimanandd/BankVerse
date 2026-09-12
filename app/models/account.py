from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship

from app.models.base import Base

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)

    account_number = Column(String, unique=True, nullable=False, index=True)

    balance = Column(Numeric(12,2), default=0)

    user_id = Column(Integer, ForeignKey("users.id"), unique=True)

    user = relationship("User", back_populates="account") 

    