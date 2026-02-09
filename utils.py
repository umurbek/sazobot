import html

def esc(s: str | None) -> str:
    return html.escape(s or "")

def short_title(t: str, n: int = 44) -> str:
    t = (t or "").strip()
    if len(t) <= n:
        return t
    return t[: n - 1] + "…"
