from aiogram.filters import BaseFilter
from aiogram.types import Message

from app.database.requests.requests import is_admins_id

class IsAdmin(BaseFilter):
    async def __call__(self, message: Message):
        return await is_admins_id(message.from_user.id)