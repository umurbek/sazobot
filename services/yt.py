import uuid
from pathlib import Path
from typing import Any
from yt_dlp import YoutubeDL

from config import DOWNLOAD_DIR, FFMPEG_PATH

def _ydl_base_opts():
    return {
        "quiet": True,
        "no_warnings": True,
        "noplaylist": True,
        "cachedir": False,
        "extractor_args": {
            "youtube": {
                "player_client": ["android"],
                "skip": ["dash", "hls"],
            }
        },
    }

def search_youtube(query: str, limit: int = 20):
    opts = _ydl_base_opts()
    opts.update({
        "skip_download": True,
        "extract_flat": "in_playlist",
    })
    with YoutubeDL(opts) as ydl:
        info = ydl.extract_info(f"ytsearch{limit}:{query}", download=False)

    out: list[dict[str, Any]] = []
    for e in info.get("entries") or []:
        if not e:
            continue
        out.append({
            "title": e.get("title"),
            "uploader": e.get("uploader"),
            "duration": int(e.get("duration") or 0),
            "url": e.get("webpage_url") or e.get("url"),
        })
    return [x for x in out if x.get("url")]

def download_fast(url: str):
    job = uuid.uuid4().hex
    opts = _ydl_base_opts()
    opts.update({
        "format": "bestaudio/best",
        "merge_output_format": "m4a",
        "outtmpl": str(DOWNLOAD_DIR / f"{job}.%(ext)s"),
    })
    with YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=True)
        path = Path(ydl.prepare_filename(info))
        return (
            str(path),
            info.get("title") or "Unknown",
            info.get("uploader") or "",
            int(info.get("duration") or 0),
        )

def download_mp3(url: str, q: str):
    job = uuid.uuid4().hex
    opts = _ydl_base_opts()
    opts.update({
        "format": "bestaudio/best",
        "outtmpl": str(DOWNLOAD_DIR / f"{job}.%(ext)s"),
        "ffmpeg_location": FFMPEG_PATH,
        "postprocessors": [
            {"key": "FFmpegExtractAudio", "preferredcodec": "mp3", "preferredquality": q}
        ],
    })
    with YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=True)
        mp3 = Path(ydl.prepare_filename(info)).with_suffix(".mp3")
        return str(mp3), info.get("title") or "Unknown", info.get("uploader") or "", int(info.get("duration") or 0)
