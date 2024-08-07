from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import KeyboardButton, InlineKeyboardButton

async def main_menu():
    keyboard = ReplyKeyboardBuilder()
    keyboard.add(KeyboardButton(text='Создать рассылку')).add(KeyboardButton(text='Добавить канал для рассылки'))
    return keyboard.adjust(2).as_markup(resize_keyboard = True, one_time_keyboard = True)

async def get_post_menu():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Да', callback_data='yes')).add(InlineKeyboardButton(text='Нет', callback_data='no'))
    return keyboard.adjust(2).as_markup()

async def check(button, url):
    if button and url:
        keyboard = InlineKeyboardBuilder()
        keyboard.add(InlineKeyboardButton(text=button, url=url))
        return keyboard.adjust(1).as_markup()
    else:
        return None

async def check_menu():
    keyboard = ReplyKeyboardBuilder()
    keyboard.add(KeyboardButton(text='Да')).add(KeyboardButton(text='Нет'))
    return keyboard.adjust(2).as_markup(resize_keyboard = True, one_time_keyboard = True)
