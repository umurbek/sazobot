from aiogram import Router, types
from aiogram.filters import Command

from keyboards.reply import main_kb
from utils import esc

router = Router()

@router.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "🎵 <b>Music Search Bot</b>\n\n"
        "Qo‘shiq nomini yozing — topib beraman.\n\n"
        "Misol:\n<code>Imagine Dragons Believer</code>",
        parse_mode="HTML",
        reply_markup=main_kb,
    )
