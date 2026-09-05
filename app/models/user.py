from sqlalchemy import String

from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import BaseModel

class User(BaseModel):
    __tablename__="users"

    full_name: Mapped[str] = mapped_column(String(100))

    email: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )

    phone_number: Mapped[str] = mapped_column(
        String(15),
        unique=True
    )

    hashed_password: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    