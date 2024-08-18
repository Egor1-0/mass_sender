from aiogram import F, Router
from aiogram.types import Message

from app.keyboards.profile_keyboard import main_profile_menu, delete_channel, subscription_
from app.keyboards.user_keyboard import main_menu
from app.database import db

profile_router = Router()


@profile_router.message(F.text == 'Профиль⚙️')
async def profile(message: Message):
    await message.answer('Выберите пункт меню', reply_markup=main_profile_menu())


@profile_router.message(F.text == 'Подписка')
async def subscription(message: Message):
    if db.check_user_status(message.from_user.id)[0]:
        await message.answer('Подписка оформлена', reply_markup=main_menu())
    else:
        await message.answer('Подписка не оформлена', reply_markup=subscription_())


@profile_router.message(F.text == 'Назад')
async def back(message: Message):
    await message.answer('Выберите пункт меню', reply_markup=main_profile_menu())


@profile_router.message(F.text == 'Купить подписку')
async def buy(message: Message):
    # здесь типа будет покупка дальше. а пока просто активация акка
    db.set_user_status(message.from_user.id, True)
    await message.answer('Подписка куплена', reply_markup=main_menu())


@profile_router.message(F.text == 'Мои каналы')
async def profile(message: Message):
    channels = db.get_channels(message.from_user.id)
    for channel in channels:
        await message.answer(str(channel[2]), reply_markup=delete_channel(channel[0]))
    
    await message.answer('Выберите пункт меню', reply_markup=main_menu())