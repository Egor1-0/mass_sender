from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from app.keyboards.reg_keyboard import main_reg_menu
from app.database import db
from app.filters.is_payed import IsPayed


reg_router = Router()

@reg_router.message(CommandStart())
async def start(message: Message):
    if not db.check_user(message.from_user.id):
        db.add_user(message.from_user.id)
    await message.answer('Выберите кнопки', reply_markup=main_reg_menu())


@reg_router.message(~IsPayed())
async def nothing(message: Message):
    await message.answer('Неизвестное действие. Выберите кнопки', reply_markup=main_reg_menu())