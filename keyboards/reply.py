from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

BTN_SEARCH = "🎵 Qidirish"
BTN_HELP = "ℹ️ Yordam"
BTN_CLEAR = "🧹 Tozalash"

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=BTN_SEARCH)],
        [KeyboardButton(text=BTN_HELP), KeyboardButton(text=BTN_CLEAR)],
    ],
    resize_keyboard=True,
)
