from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.models.base_model import Base

class Admin_id(Base):
    __tablename__ = 'admins_id'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    admin_id: Mapped[str] = mapped_column(String(15))

class Channel_id(Base):
    __tablename__ = 'channels_id'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    channel_id: Mapped[str] = mapped_column(String(20))