from app.database.models.models import Admin_id, Channel_id
from app.database.session.create_session import async_session
from sqlalchemy import select

async def add_channel_(id_channel):
    async with async_session() as session:
        session.add(Channel_id(channel_id = id_channel))
        await session.commit()