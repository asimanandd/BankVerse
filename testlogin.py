from app.utils.security import verify_password

hashed = input("Paste hashed password: ")
password = input("Password: ")

print(verify_password(password, hashed))