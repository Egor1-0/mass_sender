from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from app.keyboards.reg_keyboard import main_reg_menu

from app.database import db

user_registration = Router()

@user_registration.message(CommandStart())
async def start(message: Message):
    if db.check_user(message.from_user.id):
        pass
    else:
        db.add_user(message.from_user.id)
    await message.answer('Привет. Выбери кнопки', reply_markup=await main_reg_menu())


@user_registration.message(F.text == 'Профиль')
async def profile(message: Message):
    await message.answer('profile')


@user_registration.message(F.text == 'Оформить подписку')
async def profile(message: Message):
    db.set_status(message.from_user.id, True)
    await message.answer('sometext')


@user_registration.message()
async def nothing(message: Message):
    await message.answer('Неизвестное действие. Выберите кнопки', reply_markup=await main_reg_menu())