import time

from app.queries import brute_force, redis_cached


def measure_time(func, *args, **kwargs):
    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()
    return result, round((end - start) * 1000, 2)  # milliseconds


def compare_lookup(email: str) -> dict:
    # Brute lookup
    start = time.time()
    brute_result = brute_force.check_user(email)
    brute_time = (time.time() - start) * 1000

    # Cached lookup
    start = time.time()
    cached_result, was_cached = redis_cached.check_user(email)  # update here
    cached_time = (time.time() - start) * 1000

    return {
        "brute": {"result": brute_result, "time_ms": round(brute_time, 2)},
        "cached": {
            "result": cached_result,
            "time_ms": round(cached_time, 2),
            "hit": was_cached,  # include cache status
        },
    }


def benchmark_n_times(email: str, n: int = 5):
    brute_times = []
    cached_times = []

    for _ in range(n):
        _, brute_time = measure_time(brute_force.check_user, email)
        (_, _), cached_time = measure_time(
            redis_cached.check_user, email
        )  # unpack safely

        brute_times.append(brute_time)
        cached_times.append(cached_time)

    return {
        "email": email,
        "samples": n,
        "brute_avg": round(sum(brute_times) / n, 2),
        "cached_avg": round(sum(cached_times) / n, 2),
        "brute_times": brute_times,
        "cached_times": cached_times,
    }
