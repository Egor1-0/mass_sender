from aiogram.filters import BaseFilter
from aiogram import types


class ChatTypesFilter(BaseFilter):
    def __init__(self, chat_types: list[str] | str) -> None:
        self.chat_types = chat_types

    async def __call__(self, messange: types.Message) -> bool:
        if isinstance(self.chat_types, str):
            return messange.chat.type == self.chat_types
        else:
            return messange.chat.type in self.chat_types
