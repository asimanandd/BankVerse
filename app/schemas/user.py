from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    full_name: str = Field(min_length=3, max_length=100)

    email: EmailStr

    phone_number: str = Field(
        min_length=10,
        max_length=15
    )

    password: str = Field(
        min_length=8,
        max_length=128
    )