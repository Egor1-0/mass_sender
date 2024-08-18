from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from app.filters.is_payed import IsPayed
from app.keyboards.user_keyboard import main_menu

from app.database import db

user_router = Router()

user_router.message.filter(IsPayed())

@user_router.message(CommandStart())
async def start(message: Message):
    await message.answer('Выберите кнопки⌨️', reply_markup=await main_menu())


@user_router.message()
async def nothing(message: Message):
    await message.answer('Неизвестное действие. Выберите кнопки⌨️', reply_markup=await main_menu())