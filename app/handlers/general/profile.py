from aiogram import F, Router
from aiogram.types import Message

from app.filters.is_payed import IsPayed
from app.keyboards.profile_keyboard import main_profile_menu
from app.keyboards.user_keyboard import main_menu
from app.database import db

profile_router = Router()


@profile_router.message(F.text == 'Профиль⚙️')
async def profile(message: Message):
    await message.answer('Выберите пункт меню', reply_markup=await main_profile_menu())


@profile_router.message(F.text == 'Подписка')
async def subscription(message: Message):
    if db.check_user_status(message.from_user.id)[0]:
        await message.answer('Подписка уже оформлена', reply_markup=await main_menu())
    else:
        db.set_user_status(message.from_user.id, True)
        await message.answer('Подписка успешно оформлена', reply_markup=await main_menu())


@profile_router.message(F.text == 'Мои каналы')
async def profile(message: Message):
    channels = db.get_channels(message.from_user.id)
    for channel in channels:
        await message.answer(str(channel[0]))