import uuid
from decimal import Decimal

from sqlalchemy.orm import Session
from app.models.transactions import Transaction

class TransactionService:

    @staticmethod
    def create_transaction(
        db: Session,
        transaction_type: str,
        amount: Decimal,
        sender_account_id: int | None = None,
        receiver_account_id: int | None = None,
        status: str = "SUCCESS"
    ):

        transaction = Transaction(
            transaction_reference=f"BANK-{uuid.uuid4().hex[:12].upper()}",
            sender_account_id=sender_account_id,
            receiver_account_id=receiver_account_id,
            transaction_type=transaction_type,
            amount=amount,
            status=status
        )

        db.add(transaction)

        return transaction

    @staticmethod
    def get_transactions_by_account(
        db: Session,
        account_id: int
    ):

        return (
            db.query(Transaction)
            .filter(
                (Transaction.sender_account_id == account_id)
                |
                (Transaction.receiver_account_id == account_id)
            )
            .order_by(Transaction.created_at.desc())
            .all()
        )
    