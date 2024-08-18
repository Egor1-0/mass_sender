from aiogram import Router

from app.handlers.general import user_state_general
from app.handlers.user import user

handler = Router()

handler.include_routers(user, user_state_general)