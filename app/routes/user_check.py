from fastapi import APIRouter

from app.queries import brute_force, redis_cached

router = APIRouter()


@router.get("/brute")
def brute_check(email: str):
    return {"exists": brute_force.check_user(email)}


@router.get("/cached")
def cached_check(email: str):
    return {"exists": redis_cached.check_user(email)}


@router.delete("/cache/flush")
def clear_redis_cache():
    redis_cached.clear_cache()
    return {"status": "Cache cleared"}
