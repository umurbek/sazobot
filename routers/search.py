import asyncio
from aiogram import Router, types
from aiogram.exceptions import TelegramBadRequest

from keyboards.reply import BTN_SEARCH, BTN_HELP, BTN_CLEAR
from keyboards.inline import build_list_keyboard
from state import get_state, clear_state
from utils import esc
from services.yt import search_youtube
from services.cache import TTLCache
from config import PAGE_SIZE, MAX_PAGES, DEFAULT_MODE, SEARCH_TTL

router = Router()

# cache + concurrency (router-level)
cache = TTLCache(SEARCH_TTL)

@router.message(lambda m: (m.text or "") == BTN_HELP)
async def help_msg(message: types.Message):
    await message.answer(
        "ℹ️ Faqat qo‘shiq nomidan qidiradi.\n"
        "YouTube → M4A (tez) yoki MP3.\n\n"
        "⚡ Tezlik uchun yuklash navbat bilan ishlaydi."
    )

@router.message(lambda m: (m.text or "") == BTN_CLEAR)
async def clear(message: types.Message):
    clear_state(message.from_user.id)
    await message.answer("🧹 Tozalandi")

@router.message()
async def search_handler(message: types.Message):
    text = (message.text or "").strip()
    if not text or text in {BTN_SEARCH, BTN_HELP, BTN_CLEAR}:
        return

    uid = message.from_user.id
    st = get_state(uid, DEFAULT_MODE)
    st["query"] = text
    st["page"] = 0

    status = await message.answer("🔎 Qidiryapman...")

    key = text.lower().strip()
    results = cache.get(key)

    try:
        if results is None:
            results = await asyncio.to_thread(search_youtube, text, 20)
            cache.set(key, results)
    except Exception as e:
        await status.edit_text(f"❌ Qidirishda xatolik: <code>{esc(str(e))}</code>", parse_mode="HTML")
        return

    if not results:
        await status.edit_text("❌ Topilmadi")
        return

    st["results"] = results[: PAGE_SIZE * MAX_PAGES]

    try:
        await status.edit_text(
            f"✅ <b>Natijalar</b>\n<code>{esc(text)}</code>\n\n"
            f"Rejim: <b>{esc(st['mode'])}</b>",
            parse_mode="HTML",
            reply_markup=build_list_keyboard(uid, DEFAULT_MODE),
        )
    except TelegramBadRequest:
        await message.answer(
            f"✅ <b>Natijalar</b>\n<code>{esc(text)}</code>\n\n"
            f"Rejim: <b>{esc(st['mode'])}</b>",
            parse_mode="HTML",
            reply_markup=build_list_keyboard(uid, DEFAULT_MODE),
        )
