from sqlalchemy.orm import Session
from sqlalchemy.orm import Session
from app.models.user import User
from app.models.user import User
from app.schemas.user import UserCreate
from app.utils.security import hash_password

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
        return db_user
    