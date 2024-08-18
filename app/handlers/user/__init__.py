from aiogram import Router

from app.handlers.user.user_state import user_state_create_sending
from app.handlers.user.user import user_router
from app.handlers.user.user_add_channel import user_state_add_channel
from app.handlers.user.user_delete_channel import user_callback_delete_channel
from app.filters.chattype import ChatTypesFilter

user = Router()

user.message.filter(ChatTypesFilter(['private']))

user.include_routers(user_state_add_channel, user_callback_delete_channel, user_state_create_sending, user_router)