from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from app.filters.isadminfilter import IsAdmin
from app.keyboards.admin_keyboard import main_menu

admin_handler = Router()

admin_handler.message.filter(IsAdmin())

@admin_handler.message(CommandStart())
async def start(message: Message):
    await message.answer('Привет. Выбери кнопки', reply_markup=await main_menu())


@admin_handler.message()
async def nothing(message: Message):
    await message.answer('Неизвестное действие. Выберите кнопки', reply_markup=await main_menu())