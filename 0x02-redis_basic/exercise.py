#!/usr/bin/env python3
"""a class that defines a redis instance
    using a cache database"""
import redis
import uuid
from typing import Callable, Union
from functools import wraps


def count_calls(method: Callable) -> Callable:
    '''count how many times methods of Cache class are called'''
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''wrap the decorated function and return the wrapper'''
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """create a redis instance and cache"""
    def __init__(self) -> None:
        """initialize the cache class"""
        self._redis: redis.Redis = redis.Redis()
        self._redis.flushdb(True)

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes and stores data in redis"""
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self,
            key: str,
            fn: Callable = None) -> Union[str, bytes, int, float]:
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
