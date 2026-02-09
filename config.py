import os
from pathlib import Path

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("TELEGRAM_BOT_TOKEN topilmadi")

FFMPEG_PATH = os.getenv("FFMPEG_PATH", r"C:\ffmpeg\bin")

DOWNLOAD_DIR = Path("downloads")
DOWNLOAD_DIR.mkdir(exist_ok=True)

PAGE_SIZE = 10
MAX_PAGES = 2
DEFAULT_MODE = "fast"

SEARCH_TTL = 300  # 5 min

# PERFORMANCE LIMITS
SEARCH_CONCURRENCY = 3
DOWNLOAD_CONCURRENCY = 1
