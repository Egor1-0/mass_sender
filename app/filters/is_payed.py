from aiogram.filters import BaseFilter
from aiogram.types import Message

from app.database import db

class IsPayed(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        status = db.check_user_status(message.from_user.id)
        if status:
            return bool(status[0])
        else:
            return False