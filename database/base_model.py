from typing import Optional

from config import DATABASE_URL

from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, AsyncAttrs, async_sessionmaker, AsyncSession

engine = create_async_engine(url=DATABASE_URL)
async_session: Optional[AsyncSession] = async_sessionmaker(bind=engine, class_=AsyncSession)
metadata = MetaData()


class Base(AsyncAttrs, DeclarativeBase):
    pass