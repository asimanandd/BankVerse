import uuid
from decimal import Decimal

from sqlalchemy import String, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import BaseModel

class Transaction(BaseModel):
    __tablename__ = "transactions"

    transaction_reference: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
        index=True
    )

    sender_account_id: Mapped[int | None] = mapped_column(
        ForeignKey("accounts.id"),
        nullable=True
    )

    receiver_account_id: Mapped[int | None] = mapped_column(
        ForeignKey("accounts.id"),
        nullable=True
    )

    transaction_type: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    amount: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False   
    )

    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="SUCCESS"
    )
    