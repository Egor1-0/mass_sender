from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from app.filters.is_payed import IsPayed
from app.keyboards.user_keyboard import main_menu

from app.database import db

user = Router()

user.message.filter(IsPayed())

@user.message(CommandStart())
async def start(message: Message):
    await message.answer('Выберите кнопки', reply_markup=await main_menu())

@user.message()
async def nothing(message: Message):
    await message.answer('Неизвестное действие. Выберите кнопки', reply_markup=await main_menu())