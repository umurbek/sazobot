from typing import Any

STATE: dict[int, dict[str, Any]] = {}

def get_state(uid: int, default_mode: str) -> dict[str, Any]:
    if uid not in STATE:
        STATE[uid] = {
            "query": "",
            "results": [],
            "page": 0,
            "mode": default_mode,
            "quality": "192",
        }
    return STATE[uid]

def clear_state(uid: int):
    STATE.pop(uid, None)
