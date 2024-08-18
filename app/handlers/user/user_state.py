from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from app.filters.is_payed import IsPayed
from app.keyboards.user_keyboard import main_menu, get_post_menu, check, check_menu
from app.states.states import Сhannel, Post

from app.database import db

user_state_create_sending = Router()

user_state_create_sending.message.filter(IsPayed())

@user_state_create_sending.message(F.text == 'Создать рассылку')
async def create_newsletter(message: Message, state: FSMContext):
    await state.set_state(Post.get_post)
    await message.answer('Отправьте сообщение💬, которое будет рассылаться. Оно может содержать любой медиа-материал.')


@user_state_create_sending.message(Post.get_post)
async def get_post(message: Message, state: FSMContext):
    await state.update_data(get_post = message.message_id)
    await message.answer('Добавлять кнопку-ссылку?', reply_markup=get_post_menu())


@user_state_create_sending.callback_query(F.data == 'yes')
async def add_buttons(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(None)
    await state.set_state(Post.get_button_text)
    await callback.answer('Вы нажали "Да"☑️')
    await callback.message.answer('Введите текст кнопки⌨️')


@user_state_create_sending.callback_query(F.data == 'no')
async def add_buttons(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(None)

    await state.update_data(get_button_text = None)
    await state.update_data(get_button_url = None)

    await callback.answer('Вы нажали "нет"❌')

    data = await state.get_data()
    await callback.message.bot.copy_message(chat_id=callback.message.chat.id, from_chat_id=callback.message.chat.id, message_id=data['get_post'], 
                                   reply_markup=check(data['get_button_text'], data['get_button_url']))
    
    await state.set_state(Post.check)

    await callback.message.answer('Все правильно?', reply_markup=check_menu())


@user_state_create_sending.message(Post.get_button_text)
async def get_button_text(message: Message, state: FSMContext):
    await state.update_data(get_button_text = message.text)
    await state.set_state(Post.get_button_url)

    await message.answer('Отправьте ссылку, на которую будет кидать пользователя при нажатии на кнопку')


@user_state_create_sending.message(Post.get_button_url)
async def get_button_url(message: Message, state: FSMContext):
    await state.update_data(get_button_url = message.text)
    await state.set_state(Post.check)

    data = await state.get_data()
    await message.bot.copy_message(chat_id=message.chat.id, from_chat_id=message.chat.id, message_id=data['get_post'], 
                                   reply_markup=check(data['get_button_text'], data['get_button_url']))
    
    await message.answer('Все правильно?', reply_markup=check_menu())


@user_state_create_sending.message(Post.check,  F.text == 'Да')
async def get_button_url(message: Message, state: FSMContext):
    channel_ids = db.get_channels(message.from_user.id)

    data = await state.get_data()

    for channel_id in channel_ids:
        print(channel_id[0])
        # try:
        await message.bot.copy_message(chat_id=channel_id[0], from_chat_id=message.chat.id, 
                                           message_id=data['get_post'], reply_markup=check(data['get_button_text'], data['get_button_url']))
        # except:
        #     continue

    await state.clear()
    
    await message.answer('Рассылка завершена☑️. Выбери кнопки⌨️', reply_markup=main_menu())


@user_state_create_sending.message(Post.check,  F.text == 'Нет')
async def clear(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('Рассылка отменена❌. Выбери кнопки⌨️', reply_markup=main_menu())