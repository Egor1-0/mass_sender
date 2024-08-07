import os
import logging
import asyncio

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from app.handlers.handler import router
from app.handlers.admin import admin
from app.database.session.create_session import async_main

load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

async def main():
    await async_main()
    dp.include_routers(admin, router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass