import random
from decimal import Decimal
from sqlalchemy.orm import Session
from app.services.transaction_service import TransactionService
from app.models.account import Account
from app.models.user import User

class AccountService:

    @staticmethod
    def generate_account_number(db: Session):

        while True:

            account_number = str(
                random.randint(1000000000, 9999999999)
            )

            existing = (
                db.query(Account)
                .filter(Account.account_number == account_number)
                .first()
            )

            if not existing:
                return account_number


    @staticmethod
    def create_account(db: Session, user_id: int):

        account = Account(
            account_number=AccountService.generate_account_number(db),
            balance=0,
            user_id=user_id
        )

        db.add(account)
        db.commit()
        db.refresh(account)

        return account


    @staticmethod
    def get_account_by_user(db: Session, user_id: int):

        return (
            db.query(Account)
            .filter(Account.user_id == user_id)
            .first()
        )


    @staticmethod
    def deposit(db: Session, user_id: int, amount: float):

        account = (
            db.query(Account)
            .filter(Account.user_id == user_id)
            .first()
        )

        if not account:
            raise ValueError("Bank account not found")

        account.balance += amount

        TransactionService.create_transaction(
            db=db,
            account_id=account.id,
            transaction_type="DEPOSIT",
            amount=amount
        )

        db.commit()
        db.refresh(account)
        return account

    @staticmethod
    def withdraw(db: Session, user_id: int, amount: Decimal):

        account = (
            db.query(Account)
            .filter(Account.user_id == user_id)
            .first()
        )

        if not account:
            raise ValueError("Bank account not found")

        if account.balance < amount:
            raise ValueError("Insufficient balance")
        account.balance -= amount

        TransactionService.create_transaction(
            db=db,
            account_id=account.id,
            transaction_type="WITHDRAW",
            amount=amount
        )

        db.commit()
        db.refresh(account)

        return account

    @staticmethod
    def transfer(
        db: Session,
        sender_user_id: int,
        receiver_account_number: str,
        amount: Decimal
    ):
        sender_account = (
            db.query(Account)
            .filter(Account.user_id == sender_user_id)
            .first()
        )

        if not sender_account:
            raise ValueError("Sender account not found")

        receiver_account = (
            db.query(Account)
            .filter(
                Account.account_number == receiver_account_number
            )
            .first()
        )

        if not receiver_account:
            raise ValueError("Receiver account not found")

        if sender_account.id == receiver_account.id:
            raise ValueError("Cannot transfer money to your own account")

        if sender_account.balance < amount:
            raise ValueError("Insufficient Balance")

        try:

            sender_account.balance -= amount
            receiver_account.balance += amount

            TransactionService.create_transaction(
                db=db,
                transaction_type="TRANSFER",
                amount=amount,
                sender_account_id=sender_account.id,
                receiver_account_id=receiver_account.id
            )

            db.commit()

            db.refresh(sender_account)
            db.refresh(receiver_account)

            return sender_account, receiver_account

        except Exception:
            db.rollback()
            raise
        