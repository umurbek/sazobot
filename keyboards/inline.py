from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import PAGE_SIZE, MAX_PAGES
from state import get_state
from utils import short_title

def build_list_keyboard(uid: int, default_mode: str) -> InlineKeyboardMarkup:
    st = get_state(uid, default_mode)
    page = int(st.get("page") or 0)

    start = page * PAGE_SIZE
    end = min(start + PAGE_SIZE, len(st["results"]))
    rows: list[list[InlineKeyboardButton]] = []

    for i in range(start, end):
        title = short_title(st["results"][i].get("title") or "No title")
        rows.append([
            InlineKeyboardButton(
                text=f"{i+1}. {title}",
                callback_data=f"pick:{i}"
            )
        ])

    rows.append([
        InlineKeyboardButton(
            text=("✅ ⚡ M4A" if st["mode"] == "fast" else "⚡ M4A"),
            callback_data="mode:fast",
        ),
        InlineKeyboardButton(
            text=("✅ 🎧 MP3" if st["mode"] == "mp3" else "🎧 MP3"),
            callback_data="mode:mp3",
        ),
    ])

    max_items = PAGE_SIZE * MAX_PAGES
    total = min(len(st["results"]), max_items)
    last_page = max((total - 1) // PAGE_SIZE, 0)

    nav_row: list[InlineKeyboardButton] = []
    if page > 0:
        nav_row.append(InlineKeyboardButton(text="⬅️ Oldingi", callback_data="page:prev"))
    nav_row.append(InlineKeyboardButton(text=f"📄 {page+1}/{last_page+1}", callback_data="noop"))
    if page < last_page:
        nav_row.append(InlineKeyboardButton(text="Keyingi ➡️", callback_data="page:next"))

    if nav_row:
        rows.append(nav_row)

    return InlineKeyboardMarkup(inline_keyboard=rows)
