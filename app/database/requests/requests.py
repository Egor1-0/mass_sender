from app.database.models.models import Admin_id, Channel_id
from app.database.session.create_session import async_session
from sqlalchemy import select

async def is_admins_id(user):
    async with async_session() as session:
        return await session.scalar(select(Admin_id).where(Admin_id.admin_id == user))
    
async def get_channel_ids():
    async with async_session() as session:
        return await session.scalars(select(Channel_id))