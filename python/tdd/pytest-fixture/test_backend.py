import random

import pytest
from redis import Redis

from backends import RedisBackend, CounterBackend
from interfaces import ViewsStorageBackend


@pytest.fixture
def counter_backend():
    return CounterBackend()


# session 스코프는 일종의 글로벌 스코프로서, 이 스코프의 픽스처는 러너가 시행되는 과정 동안 유지되며 마지막 테스트 케이스가 실
@pytest.fixture(scope="session")
def redis_client():
    return Redis(host="localhost", port=6379)


@pytest.fixture
def redis_backend(redis_client: Redis):
    set_name = "test-page-counts"
    redis_client.delete(set_name)

    return RedisBackend(redis_client=redis_client, set_name=set_name)


@pytest.fixture(params=["redis_backend", "counter_backend"])
def backend(request):
    return request.getfixturevalue(request.param)


@pytest.mark.parametrize("n", [0] + [random.randint(0, 100) for _ in range(5)])
def test_empty_backend(backend: ViewsStorageBackend, n: int):
    assert backend.most_common(n) == {}


def test_increments_all(backend: ViewsStorageBackend):
    increments = {
        "key_a": random.randint(1, 10),
        "key_b": random.randint(1, 10),
        "key_c": random.randint(1, 10),
    }

    for key, count in increments.items():
        for _ in range(count):
            backend.increment(key)

    assert backend.most_common(len(increments)) == increments
    assert backend.most_common(len(increments) + 1) == increments


def test_increments_top(backend: ViewsStorageBackend):
    increments = {
        "key_a": random.randint(1, 10),
        "key_b": random.randint(1, 10),
        "key_c": random.randint(1, 10),
        "key_d": random.randint(1, 10),
    }

    for key, count in increments.items():
        for _ in range(count):
            backend.increment(key)

    assert len(backend.most_common(1)) == 1
    assert len(backend.most_common(2)) == 2
    assert len(backend.most_common(3)) == 3

    top2_values = backend.most_common(2).values()
    assert list(top2_values) == (sorted(increments.values(), reverse=True)[:2])
