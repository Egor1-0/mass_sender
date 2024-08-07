from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from app.database.models.models import Base

engine = create_async_engine(url='mysql+asyncmy://root:123456789@localhost/masssender')
async_session = async_sessionmaker(engine, expire_on_commit=False)

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)