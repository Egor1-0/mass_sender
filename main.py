import os
import logging
import asyncio

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from app.handlers import handler
from app.states.user_state import user_state_general


load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

async def main():
    dp.include_routers(user_state_general, handler)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass