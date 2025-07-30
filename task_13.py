from dataclasses import dataclass
from functools import wraps
from time import sleep, time
from typing import Callable, Any
from threading import Lock, Thread


@dataclass
class MemoryEntry:
    value: Any
    expired_at: float


class CacheManager:
    def __init__(
        self, func: Callable, max_size: Any = None, seconds: Any = None
    ) -> None:
        self._memory: dict[tuple, MemoryEntry] = {}
        self._func: Callable = func
        self._max_size: int = self.sanitize_int_args(max_size)
        self._seconds: int = self.sanitize_int_args(seconds)
        self._lock = Lock()

        if self._seconds != -1:
            Thread(target=self.delete_expired, daemon=True).start()

    def find_or_call(self, args: tuple, kwargs: dict[str, Any]) -> Any:
        key = self.args_to_tuple(args, kwargs)

        # If record is in memory, update time and return
        with self._lock:
            record = self._memory.get(key)
            if record is not None:
                record.expired_at = time() + self._seconds
                return record.value

        # Else call a func and make a memeory entry
        res = self._func(*args, **kwargs)

        with self._lock:
            self.delete_oldest_if_needed()
            self._memory[key] = MemoryEntry(res, time() + self._seconds)

        return res

    def delete_oldest_if_needed(self) -> None:
        if self._max_size == -1 or len(self._memory) <= self._max_size - 1:
            return

        oldest_key = None
        oldest_time: float = 0
        for k, v in self._memory.items():
            if oldest_key == None:
                oldest_key = k
                oldest_time = v.expired_at
                continue

            if oldest_time > v.expired_at:
                oldest_key = k
                oldest_time = v.expired_at

        if oldest_key == None:
            return

        del self._memory[oldest_key]

    def delete_expired(self) -> None:
        while True:
            sleep(self._seconds / 2)
            to_delete = []
            with self._lock:
                for k, v in self._memory.items():
                    if v.expired_at < time():
                        to_delete.append(k)

                for k in to_delete:
                    del self._memory[k]

    @staticmethod
    def sanitize_int_args(arg: Any) -> int:
        if not isinstance(arg, int):
            return -1
        if arg <= 0:
            return -1
        return arg

    @staticmethod
    def args_to_tuple(args: tuple, kwargs: dict) -> tuple:
        return (args, tuple(sorted(kwargs.items())))


def cached(max_size=None, seconds=None):
    def inner(func):
        cache = CacheManager(func, max_size, seconds)

        @wraps(func)
        def wrapper(*args, **kwargs):
            res = cache.find_or_call(args, kwargs)
            return res

        return wrapper

    return inner
