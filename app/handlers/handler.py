from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message()
async def passs(message: Message):
    await message.answer(f'У вас нет прав чтобы писать здесь сообщения, {message.from_user.id}')