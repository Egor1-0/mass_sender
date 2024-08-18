from aiogram import Router

from app.states.user_state.user_state import user_state_create_sending
from app.states.user_state.user_add_channel import user_state_add_channel 
from app.filters.chattype import ChatTypesFilter

user_state_general = Router()

user_state_general.message.filter(ChatTypesFilter(['private']))

user_state_general.include_routers(user_state_create_sending, user_state_add_channel)