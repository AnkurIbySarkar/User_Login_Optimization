# tests/test_brute_force.py

import pytest
from app.queries.brute_force import check_user


@pytest.fixture
def seed_test_data():
    from app.database import engine, SessionLocal
    from app.models import Base, User

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    session = SessionLocal()
    session.add_all([
        User(email="alice@example.com", username="alice"),
        User(email="bob@example.com", username="bob"),
    ])
    session.commit()
    session.close()


@pytest.mark.usefixtures("seed_test_data")
def test_known_user_exists():
    assert check_user("alice@example.com") is True


@pytest.mark.usefixtures("seed_test_data")
def test_unknown_user_does_not_exist():
    assert check_user("charlie@example.com") is False
