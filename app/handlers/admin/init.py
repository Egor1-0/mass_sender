from aiogram import Router

from app.handlers.admin.admin import admin_handler
from app.handlers.admin.adminstate import admin_state

admin = Router()

admin.include_routers(admin_state, admin_handler)