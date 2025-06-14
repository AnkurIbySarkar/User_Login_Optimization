from app.database import engine, SessionLocal
from app.models import Base, User
from faker import Faker
import time

fake = Faker()

def seed_users(count=1000000):
    session = SessionLocal()
    batch_size = 5000
    for i in range(0, count, batch_size):
        users = [
            User(email=fake.unique.email(), username=fake.user_name())
            for _ in range(min(batch_size, count - i))
        ]
        session.bulk_save_objects(users)
        session.commit()
        print(f"Inserted: {i + len(users)}")
    session.close()

def init_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    seed_users()

if __name__ == "__main__":
    start = time.time()
    init_db()
    print(f"Done in {round(time.time() - start, 2)}s")