import os

import redis

REDIS_HOST = os.getenv(
    "REDIS_HOST",
    "localhost" if os.getenv("GITHUB_ACTIONS") else "redis"
)

REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
