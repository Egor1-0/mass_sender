from aiogram import Router

from app.handlers.user.user_state import user_state
from app.handlers.user.user import user

admin = Router()

admin.include_routers(user_state, user)