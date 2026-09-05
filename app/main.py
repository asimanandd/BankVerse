from fastapi import FastAPI

from app.api.user import router as user_router
from app.api.auth import router as auth_router

app = FastAPI(title="BankVerse API")

app.include_router(user_router)
app.include_router(auth_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to BankVerse"
    }