from app.database import SessionLocal
from app.models import User

def check_user(email: str) -> bool:
    db = SessionLocal()
    users = db.query(User).all()
    print(f"Found {len(users)} users in DB")
    db.close()
    return any(user.email == email for user in users)