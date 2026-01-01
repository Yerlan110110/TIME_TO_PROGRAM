import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy import create_engine, text
from config import settings


# SYNC ENGINE 
sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=False,
)


# ASYNC ENGINE
async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=False,
)


def sync_test():
    with sync_engine.connect() as conn:
        res = conn.execute(text("SELECT 1, 2, 3"))
        print("sync result =", res.first())


async def async_test():
    async with async_engine.connect() as conn:
        res = await conn.execute(text("SELECT 1, 2, 3"))
        print("async result =", res.first())


def main():
    sync_test()
    asyncio.run(async_test())


if __name__ == "__main__":
    main()
