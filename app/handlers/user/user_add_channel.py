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
    await state.set_state(Сhannel.get_channel_name)
    await message.answer('Отправьте имя вашей группы или канала')


@user_state_add_channel.message(Сhannel.get_channel_name)
async def get_name_channel(message: Message, state: FSMContext):
    await state.update_data(get_channel_name = message.text)
    await state.set_state(Сhannel.get_channel_id)
    await message.answer(('Отправьте уникальный идентификатор канала или группы. Его можно узнать через веб версию телеграмма.\n'
                          +'В ссылке в строке URL в конце строки есть цифры, перед ними знак минус. Отправьте  эти цифры со знаком минус.\n'
                          +'Помните, бот не сможет отправлять сообщения, если не является участником чата.'))



@user_state_add_channel.message(Сhannel.get_channel_id)
async def get_id_channel(message: Message, state: FSMContext):
    data = await state.get_data()
    db.add_channel(message.from_user.id, message.text, data['get_channel_name'])
    await state.clear()
    await message.answer('Канал добавлен', reply_markup=main_menu())