from aiogram.filters import BaseFilter
from aiogram.types import Message

from app.database import db

class IsPayed(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return db.check_status(message.from_user.id)