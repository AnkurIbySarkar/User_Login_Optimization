import fakeredis
import pytest

import app.queries.redis_cached as redis_module
from app.database import SessionLocal
from app.models import User
from app.queries.redis_cached import check_user as real_check_user


@pytest.fixture(scope="function", autouse=True)
def setup_test_db():
    db = SessionLocal()
    db.query(User).delete()
    db.add(User(email="redisuser@example.com", username="redis_user"))
    db.commit()
    db.close()


@pytest.fixture(autouse=True)
def mock_redis(monkeypatch):
    fake = fakeredis.FakeRedis(decode_responses=True)
    monkeypatch.setattr(redis_module, "redis_client", fake)
    yield fake


def test_first_lookup_is_cache_miss():
    exists, hit = real_check_user("redisuser@example.com")
    assert exists is True
    assert hit is False  # First lookup should be DB


def test_second_lookup_is_cache_hit():
    # First call to populate cache
    real_check_user("redisuser@example.com")

    # Second call should hit Redis
    exists, hit = real_check_user("redisuser@example.com")
    assert exists is True
    assert hit is True
