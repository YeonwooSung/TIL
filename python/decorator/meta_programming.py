from functools import lru_cache


@lru_cache(size=100)
def expensive_func(a, b):
    return a + b
