from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from app.filters.is_payed import IsPayed
from app.keyboards.user_keyboard import main_menu, get_post_menu, check, check_menu
from app.states.states import Сhannel, Post

from app.database import db

user_state_add_channel = Router()

user_state_add_channel.message.filter(IsPayed())

@user_state_add_channel.message(F.text == 'Добавить канал для рассылки')
async def add_channel(message: Message, state: FSMContext):
    await state.set_state(Сhannel.get_channel)
    await message.answer(('Отправьте уникальный идентификатор канала. Его можно узнать через веб версию телеграмма.\n'
                          +'В ссылке в строке URL в конце строки есть цифры, перед ними знак минус. Отправьте  эти цифры со знаком минус.\n'
                          +'Помните, бот не сможет отправлять сообщения, если не является участником чата.'))


@user_state_add_channel.message(Сhannel.get_channel)
async def get_id_channel(message: Message, state: FSMContext):
    db.add_channel(message.from_user.id, message.text)
    await state.clear()
    await message.answer('Канал добавлен', reply_markup=await main_menu())