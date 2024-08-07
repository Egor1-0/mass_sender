from aiogram.filters import BaseFilter
from aiogram.types import Message

from app.database.requests.requests import is_admins_id

class Admin(BaseFilter):
    async def __call__(self, message: Message):
        return True if (await is_admins_id(message.from_user.id)) else False