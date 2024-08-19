import time

from aiogram.filters import BaseFilter
from aiogram.types import Message

from app.database import db

class IsPayed(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        status = db.check_user_status(message.from_user.id)
        now = int(time.time())
        print(status, now)
        if status:
            return status[0] > now
        else:
            return False