from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from config import settings


engine = create_async_engine(settings.DATABASE_URL)

