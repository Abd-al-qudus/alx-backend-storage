#!/usr/bin/env python3
"""a class that defines a redis instance
    using a cache database"""
import redis
import uuid
from typing import (
    Any,
    Callable,
    Union
)


class Cache:
    """create a redis instance and cache"""
    def __init__(self) -> None:
        """initialize the cache class"""
        self._redis: redis.Redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes and stores data in redis"""
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: Union[str, bytes, int], fn: Callable = None) -> Any:
        """get data from the redis storage"""
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """get stored string from redis cache"""
        return self.get(key, fn=lambda value: value.decode("utf-8"))

    def get_int(self, key: int) -> int:
        """get stored int from redis cache"""
        return self.get(key, fn=int)
