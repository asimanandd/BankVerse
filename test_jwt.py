from app.auth.jwt_handler import create_access_token

token = create_access_token(
    {"sub": "asim@gmail.com"}
)

print(token)