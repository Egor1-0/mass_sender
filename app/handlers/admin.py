from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from app.filters.filters import Admin
from app.keyboards.admin_keyboard import main_menu, get_post_menu, check, check_menu
from app.states.states import Get_channel, Get_post
from app.database.requests.pushes import add_channel_
from app.database.requests.requests import get_channel_ids

admin = Router()

@admin.message(CommandStart(), Admin())
async def start(message: Message):
    await message.answer('Привет. Выбери кнопки', reply_markup=await main_menu())

@admin.message(Admin(), F.text == 'Добавить канал для рассылки')
async def add_channel(message: Message, state: FSMContext):
    await state.set_state(Get_channel.get_channel)
    await message.answer("""Отправьте уникальный идентификатор канала. Его можно узнать через веб версию телеграмма.\n \
                         В ссылке в строке URL в конце строки есть цифры, перед ними знак минус. Отправьте  эти цифры со знаком минус.\n \
                         Помните, бот не сможет отправлять сообщения, если не является участником чата.""")
    
@admin.message(Admin(), Get_channel.get_channel)
async def get_id_channel(message: Message, state: FSMContext):
    await add_channel_(message.text)
    await state.clear()
    await message.answer('Канал добавлен', reply_markup=await main_menu())

@admin.message(Admin(), F.text == 'Создать рассылку')
async def create_newsletter(message: Message, state: FSMContext):
    await state.set_state(Get_post.get_post)
    await message.answer('Отправьте сообщение, которое будет рассылаться. Оно может содержать любой медиа-материал.')

@admin.message(Admin(), Get_post.get_post)
async def get_post(message: Message, state: FSMContext):
    await state.update_data(get_post = message.message_id)
    await message.answer('Добавлять кнопку-ссылку?', reply_markup=await get_post_menu())

@admin.callback_query(Admin(), F.data == 'yes')
async def add_buttons(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(None)
    await state.set_state(Get_post.get_button_text)
    await callback.answer('Вы нажали "Да"')
    await callback.message.answer('Введите текст кнопки')

@admin.callback_query(Admin(), F.data == 'no')
async def add_buttons(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(None)
    await state.update_data(get_button_text = None)
    await state.update_data(get_button_url = None)
    await callback.answer('Вы нажали "нет"')
    data = await state.get_data()
    await callback.message.bot.copy_message(chat_id=callback.message.chat.id, from_chat_id=callback.message.chat.id, message_id=data['get_post'], 
                                   reply_markup=await check(data['get_button_text'], data['get_button_url']))
    await state.set_state(Get_post.check)
    await callback.message.answer('Все правильно?', reply_markup=await check_menu())

@admin.message(Admin(), Get_post.get_button_text)
async def get_button_text(message: Message, state: FSMContext):
    await state.update_data(get_button_text = message.text)
    await state.set_state(Get_post.get_button_url)
    await message.answer('Отправьте ссылку, на которую будет кидать пользователя при нажатии на кнопку')

@admin.message(Admin(), Get_post.get_button_url)
async def get_button_url(message: Message, state: FSMContext):
    await state.update_data(get_button_url = message.text)
    await state.set_state(Get_post.check)
    data = await state.get_data()
    await message.bot.copy_message(chat_id=message.chat.id, from_chat_id=message.chat.id, message_id=data['get_post'], 
                                   reply_markup=await check(data['get_button_text'], data['get_button_url']))
    await message.answer('Все правильно?', reply_markup=await check_menu())

@admin.message(Admin(), Get_post.check,  F.text == 'Да')
async def get_button_url(message: Message, state: FSMContext):
    channel_ids = await get_channel_ids()
    data = await state.get_data()
    for channel_id in channel_ids:
        try:
            await message.bot.copy_message(chat_id=channel_id.channel_id, from_chat_id=message.chat.id, message_id=data['get_post'], reply_markup=await check(data['get_button_text'], data['get_button_url']))
        except:
            continue
    await state.clear()
    await message.answer('Рассылка завершена. Выбери кнопки', reply_markup=await main_menu())

@admin.message(Admin(), Get_post.check,  F.text == 'Нет')
async def clear(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('Рассылка отменена. Выбери кнопки', reply_markup=await main_menu())

@admin.message(Admin())
async def nothing(message: Message):
    await message.answer('Неизвестное действие. Выберите кнопки', reply_markup=await main_menu())