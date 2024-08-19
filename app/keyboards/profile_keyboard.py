from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import KeyboardButton, InlineKeyboardButton

def main_profile_menu() -> any:
    keyboard = ReplyKeyboardBuilder()
    keyboard.add(KeyboardButton(text='Подписка')).add(KeyboardButton(text='Мои каналы'))
    return keyboard.adjust(2).as_markup(resize_keyboard = True)


def delete_channel(channel_id: int):
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='Удалить', callback_data=f'delete_{channel_id}')
    return keyboard.adjust(2).as_markup(resize_keyboard = True)


def subscription_():
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text='Купить подписку').button(text='Назад')
    return keyboard.adjust(2).as_markup(resize_keyboard = True)


def buy_subscription():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='Купить подписку', pay=True)
    return keyboard.as_markup()