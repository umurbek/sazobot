import time
from typing import Any

class TTLCache:
    def __init__(self, ttl_seconds: int):
        self.ttl = ttl_seconds
        self._store: dict[str, tuple[float, Any]] = {}

    def get(self, key: str):
        v = self._store.get(key)
        if not v:
            return None
        ts, data = v
        if time.time() - ts > self.ttl:
            self._store.pop(key, None)
            return None
        return data

    def set(self, key: str, data: Any):
        self._store[key] = (time.time(), data)
