from aiogram import F, Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from app.filters.is_payed import IsPayed

from app.database import db

user_callback_delete_channel = Router()

user_callback_delete_channel.message.filter(IsPayed())

@user_callback_delete_channel.callback_query(F.data.startswith('delete_'))
async def add_channel(call: CallbackQuery, state: FSMContext):
    db.delete_channel(call.data.split('_')[1])
    await call.answer('Удалено')