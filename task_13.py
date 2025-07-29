from dataclasses import dataclass
from functools import wraps
from typing import Any, Callable
from time import sleep, time
from threading import Thread, Lock
from heapdict import heapdict

hd = heapdict()

@dataclass
class QueueEntry:
    key: tuple
    expired_at: float


@dataclass
class MemoryEntry:
    result: Any
    queue_entry: QueueEntry


class CacheManager:
    def __init__(self, func: Callable, max_size: Any, seconds: Any) -> None:
        self.__memory: dict[tuple, MemoryEntry] = {}
        self.__queue: list[QueueEntry] = []
        self.__func: Callable = func
        self.__lock = Lock()

        # -1 means unlimited
        if not isinstance(max_size, int) or max_size < 0:
            self.__max_size = -1
        else:
            self.__max_size: int = max_size

        if not isinstance(seconds, int) or seconds < 0:
            self.__seconds = -1
        else:
            self.__seconds: float = seconds
        Thread(target=self.delete_expired_thread, daemon=True).start()


    def try_add(self, args: tuple[Any, ...], kwargs: dict[str, Any]) -> Any:
        # Compute key tuple
        key = self.args_to_tuple(args, kwargs)

        with self.__lock:
            # Get record
            record = self.__memory.get(key)

            # Return result if all is good
            if record is not None:
                record.queue_entry.expired_at = time() + self.__seconds
                return record.result

        # Compute new res
        res = self.__func(*args, **kwargs)


        # Store res
        with self.__lock:
            # Free some space if overfull
            if len(self.__queue) >= self.__max_size:
                self.delete_overfull()
            q = QueueEntry(key, time() + self.__seconds)
            self.__queue.append(q)
            self.__memory[key] = MemoryEntry(res,q)

        return record

    def delete_overfull(self):
        key = self.__queue.pop(0).key
        print(f"Deleting entry: {key} due to overfull storage.")
        del self.__memory[key]

    def delete_expired_thread(self):
        while True:
            sleep(5)
            with self.__lock:
                total = len(self.__queue)
                i = 0
                while i < total:
                    if len(self.__queue) == 0:
                        break
                    entry = self.__queue[i]
                    if entry.expired_at < time():
                        print(f"Deleting entry: {entry.key} due to storage time limit.")
                        del self.__memory[entry.key]
                        del self.__queue[i]
                    else:
                        i += 1


    @staticmethod
    def args_to_tuple(
        args: tuple[Any, ...], kwargs: dict[str, Any]
    ) -> tuple[tuple, tuple]:
        return (args, tuple(sorted(kwargs.items())))


def cached(max_size=None, seconds=None):
    def inner(func):
        cache = CacheManager(func, max_size, seconds)

        @wraps(func)
        def wrapper(*args, **kwargs):
            res = cache.try_add(args, kwargs)
            return res

        return wrapper

    return inner


@cached(2, 10)
def slow_func(arg1, arg2):
    sleep(3)
    return 0


print("Uncached:")
print(slow_func(1, 2))
print("Uncached2:")
print(slow_func(1, 3))
print("Cached:")
print(slow_func(1, 2))
print("Uncached2:")
print(slow_func(1, 4))
