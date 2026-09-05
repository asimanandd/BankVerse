from app.db.session import SessionLocal

db = SessionLocal()

print("DataBase Session Created Successfully!")

db.close()

print("Database Session Closed!")

