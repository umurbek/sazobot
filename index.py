import asyncio
from aiogram import Bot, Dispatcher

from config import TOKEN
from routers import routers

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    for r in routers:
        dp.include_router(r)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
