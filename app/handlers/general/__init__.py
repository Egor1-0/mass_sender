from aiogram import Router

from app.handlers.general.profile import profile_router
from app.handlers.general.reg import reg_router
from app.filters.chattype import ChatTypesFilter

user_state_general = Router()

user_state_general.message.filter(ChatTypesFilter(['private']))

user_state_general.include_routers(profile_router, reg_router)