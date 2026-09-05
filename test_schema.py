from app.schemas.user import UserCreate

user = UserCreate(
    full_name="Asim Anand",
    email="asimanand501@gmail.com",
    phone_number="9876543210",
    password="Asim@123"
)

print(user)

