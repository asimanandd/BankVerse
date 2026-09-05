from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.schemas.user import UserCreate
from app.services.user_service import UserService

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/register")
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    try:
        created_user = UserService.create_user(db, user)

        return {
            "message": "User registered successfully",
            "user_id": created_user.id
        }

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    
    