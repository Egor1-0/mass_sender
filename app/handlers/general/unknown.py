from aiogram import F, Router
from aiogram.types import Message

from app.keyboards.reg_keyboard import main_reg_menu
from app.database import db
from app.filters.is_payed import IsPayed

unknown_router = Router()


@unknown_router.message(~IsPayed())
async def nothing(message: Message):
    await message.answer('Неизвестное действие. Выберите кнопки', reply_markup=await main_reg_menu())