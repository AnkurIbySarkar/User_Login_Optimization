from app.cache import redis_client


def increment_hit():
    redis_client.incr("metrics:cache_hits")


def increment_miss():
    redis_client.incr("metrics:cache_misses")


def get_metrics():
    return {
        "hits": int(redis_client.get("metrics:cache_hits") or 0),
        "misses": int(redis_client.get("metrics:cache_misses") or 0),
    }


def reset_metrics():
    redis_client.set("metrics:cache_hits", 0)
    redis_client.set("metrics:cache_misses", 0)
