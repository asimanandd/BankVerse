from fastapi import FastAPI

from app.db.database import engine
from app.models.base import Base
from app.models.user import User
from app.api.user import router as user_router
from app.api.auth import router as auth_router
from app.api.account import router as account_router
from app.models.account import Account
from app.models.transactions import Transaction

Base.metadata.create_all(bind=engine)

app = FastAPI(title="BankVerse API")

app.include_router(user_router)
app.include_router(auth_router)
app.include_router(account_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to BankVerse"
    }