from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.auth.dependencies import get_current_user
from app.db.dependencies import get_db
from app.models.user import User
from app.services.account_service import AccountService
from app.schemas.account import ( DepositRequest, WithdrawRequest, TransferRequest )
from app.services.transaction_service import TransactionService

router = APIRouter(
    prefix="/accounts",
    tags=["Accounts"]
)

@router.post("/deposit")
def deposit_money(
    deposit: DepositRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    try:
        account = AccountService.deposit(
            db = db,
            user_id=current_user.id,
            amount=deposit.amount
        )

        return {
            "message": "Deposit Successfull",
            "account_number": account.account_number,
            "new_balance": account.balance
        }
    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )

@router.get("/me")
def get_my_account(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    account = AccountService.get_account_by_user(
    db,
    current_user.id
)
    if not account:
        raise HTTPException(
            status_code=404,
            detail="Account not Found"
        )

    return account

@router.post("/withdraw")
def withdraw_money(
    withdraw: WithdrawRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:

        account = AccountService.withdraw(
            db=db,
            user_id=current_user.id,
            amount=withdraw.amount
        )

        return {
            "message": "Withdrawal Successful",
            "account_number": account.account_number,
            "new_balance": account.balance 
        }

    except ValueError as e:

        if str(e) == "Insufficient balance":
            raise HTTPException(
                status_code=400,
                detail=str(e)
            )

            raise HTTPException(
                status_code=404,
                detail=str(e)
            )

        
@router.get("/transactions")
def get_my_transactions(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    account = AccountService.get_account_by_user(
        db,
        current_user.id
    )

    if not account:
        raise HTTPException(
            status_code=404,
            detail="Account Not Found"
        )

    transactions = TransactionService.get_transactions_by_account(
        db=db,
        account_id=account.id
    )

    return transactions

@router.post("/transfer")
def transfer_money(
    transfer: TransferRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:

        sender_account, receiver_account = AccountService.transfer(
            db=db,
            sender_user_id=current_user.id,
            receiver_account_number=transfer.receiver_account_number,
            amount=transfer.amount
        )

        return {
            "message": "Transfer Successfull",
            "transaction_type": "TRANSFER",
            "amount": transfer.amount,
            "sender_account_number": sender_account.account_number,
            "receiver_account_number": receiver_account.account_number,
            "sender_new_balance": sender_account.balance
        }
    except ValueError as e:

        if str(e) == "Insufficient Balance":
            raise HTTPException(
                status_code=400,
                detail=str(e),
            )

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )