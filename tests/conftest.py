import pytest

from app.database import SessionLocal, engine
from app.models import Base, User


@pytest.fixture(scope="session", autouse=True)
def seed_test_data():
    print("Seeding test data...")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    session = SessionLocal()
    test_users = [
        User(email="alice@example.com", username="alice"),
        User(email="bob@example.com", username="bob"),
    ]
    session.add_all(test_users)
    session.commit()
    session.close()
