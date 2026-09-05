from app.utils.security import hash_password, verify_password

password = "Asim@123"

hashed = hash_password(password)

print("Original :", password)
print("Hashed :", hashed)

print("Verification :", verify_password(password, hashed))

