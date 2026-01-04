import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy import create_engine, text
from config import settings


# SYNC ENGINE 
sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo = True)



# ASYNC ENGINE
async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg)


def sync_get_123():
    with sync_engine.connect() as conn:
        res = conn.execute(text("SELECT 1, 2, 3"))
        print("sync result =", res.first())


async def async_get123():
    async with async_engine.connect() as conn:
        res = await conn.execute(text("SELECT 1, 2, 3"))
        print("async result =", res.first())
