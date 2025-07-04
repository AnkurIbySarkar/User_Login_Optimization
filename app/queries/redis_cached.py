from app.cache import redis_client
from app.database import SessionLocal
from app.metrics.cache_tracker import increment_hit, increment_miss
from app.models import User


def check_user(email: str) -> tuple[bool, bool]:
    key = f"user_exists:{email}"

    cached = redis_client.get(key)
    if cached is not None:
        increment_hit()
        return cached == "true", True
    # Not in Redis — check DB
    db = SessionLocal()
    user = db.query(User).filter(User.email == email).first()
    db.close()

    exists = user is not None
    redis_client.set(key, "true" if exists else "false", ex=3600)  # 1hr TTL

    increment_miss()
    return exists, False


def clear_cache():
    redis_client.flushall()
    redis_client.set("cache:hit", 0)
    redis_client.set("cache:miss", 0)
