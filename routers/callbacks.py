import asyncio
import os
from aiogram import Router, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.exceptions import TelegramBadRequest

from state import get_state
from utils import esc
from keyboards.inline import build_list_keyboard
from services.yt import download_fast, download_mp3
from config import PAGE_SIZE, MAX_PAGES, DEFAULT_MODE, DOWNLOAD_CONCURRENCY

router = Router()
DL_SEM = asyncio.Semaphore(DOWNLOAD_CONCURRENCY)

@router.callback_query(lambda c: (c.data or "").startswith("page:"))
async def page_nav(call: types.CallbackQuery):
    uid = call.from_user.id
    st = get_state(uid, DEFAULT_MODE)

    direction = (call.data or "").split(":", 1)[1]
    page = int(st.get("page") or 0)

    max_items = PAGE_SIZE * MAX_PAGES
    total = min(len(st["results"]), max_items)
    last_page = max((total - 1) // PAGE_SIZE, 0)

    if direction == "prev":
        page = max(page - 1, 0)
    elif direction == "next":
        page = min(page + 1, last_page)

    st["page"] = page

    try:
        await call.message.edit_reply_markup(reply_markup=build_list_keyboard(uid, DEFAULT_MODE))
    except TelegramBadRequest:
        pass

    await call.answer()

@router.callback_query(lambda c: (c.data or "") == "noop")
async def noop(call: types.CallbackQuery):
    await call.answer()

@router.callback_query(lambda c: (c.data or "").startswith("pick:"))
async def pick(call: types.CallbackQuery):
    uid = call.from_user.id
    st = get_state(uid, DEFAULT_MODE)

    try:
        i = int((call.data or "").split(":", 1)[1])
        r = st["results"][i]
    except Exception:
        await call.answer("Xato indeks", show_alert=True)
        return

    await call.message.answer(
        f"🎵 <b>{esc(r.get('title'))}</b>\n"
        f"👤 {esc(r.get('uploader'))}",
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[[
            InlineKeyboardButton(text="📥 Yuklab olish", callback_data=f"dl:{i}")
        ]])
    )
    await call.answer()

@router.callback_query(lambda c: (c.data or "").startswith("mode:"))
async def mode(call: types.CallbackQuery):
    st = get_state(call.from_user.id, DEFAULT_MODE)
    st["mode"] = (call.data or "").split(":", 1)[1]

    try:
        await call.message.edit_reply_markup(reply_markup=build_list_keyboard(call.from_user.id, DEFAULT_MODE))
    except TelegramBadRequest:
        pass

    await call.answer(f"Rejim: {st['mode']}")

@router.callback_query(lambda c: (c.data or "").startswith("dl:"))
async def download(call: types.CallbackQuery):
    uid = call.from_user.id
    st = get_state(uid, DEFAULT_MODE)

    try:
        i = int((call.data or "").split(":", 1)[1])
        r = st["results"][i]
        url = r.get("url")
        if not url:
            raise ValueError("URL topilmadi")
    except Exception:
        await call.answer("Xato indeks", show_alert=True)
        return

    await call.answer("🧾 Navbatga qo‘shildi...")
    status = await call.message.answer("⏳ Tayyorlanmoqda...")

    try:
        async with DL_SEM:
            await status.edit_text("⏬ Yuklanmoqda...")

            if st["mode"] == "fast":
                path, title, uploader, dur = await asyncio.to_thread(download_fast, url)
            else:
                path, title, uploader, dur = await asyncio.to_thread(download_mp3, url, st["quality"])

            await status.edit_text("📤 Telegramga yuboryapman...")

            await call.message.answer_audio(
                audio=types.FSInputFile(path),
                title=title,
                performer=uploader,
                duration=dur if dur > 0 else None,
            )

            try:
                await status.delete()
            except TelegramBadRequest:
                pass

            try:
                os.remove(path)
            except OSError:
                pass

    except Exception as e:
        await status.edit_text(f"❌ Yuklashda xatolik: <code>{esc(str(e))}</code>", parse_mode="HTML")
