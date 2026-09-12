from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.utils.security import hash_password
from app.services.account_service import AccountService

class UserService:
    @staticmethod
    def get_user_by_email(db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

    @staticmethod
    def create_user(db: Session, user: UserCreate):

        existing_user=db.query(User).filter(
            User.email == user.email
        ).first()

        if existing_user:
            raise ValueError("Email already registered")
        db_user = User(
            full_name=user.full_name,
            email=user.email,
            phone_number=user.phone_number,
            hashed_password=hash_password(user.password)
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

# Automatically create a bank account
        AccountService.create_account(
           db=db,
           user_id=db_user.id)

        return db_user
