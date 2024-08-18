from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import KeyboardButton, InlineKeyboardButton

async def main_profile_menu() -> any:
    keyboard = ReplyKeyboardBuilder()
    keyboard.add(KeyboardButton(text='Подписка')).add(KeyboardButton(text='Мои каналы')).add(KeyboardButton(text='Назад'))
    return keyboard.adjust(2).as_markup(resize_keyboard = True)