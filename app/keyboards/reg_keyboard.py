from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import KeyboardButton, InlineKeyboardButton

async def main_reg_menu() -> any:
    keyboard = ReplyKeyboardBuilder()
    keyboard.add(KeyboardButton(text='Профиль')).add(KeyboardButton(text='Оформить подписку'))
    return keyboard.adjust(2).as_markup(resize_keyboard = True, one_time_keyboard = True)


