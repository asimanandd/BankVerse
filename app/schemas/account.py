from pydantic import BaseModel, Field
from decimal import Decimal

class AccountResponse(BaseModel):
    account_number: str
    balance: float

    model_config = {
        "from_attributes": True
    }

class DepositRequest(BaseModel):
    amount: Decimal = Field(gt=0)

class WithdrawRequest(BaseModel):
    amount: Decimal = Field(gt=0)

class TransferRequest(BaseModel):
    receiver_account_number: str
    amount: Decimal = Field(gt=0)
    