# import asyncio
# from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker,AsyncSession
# from sqlalchemy.orm import Session, sessionmaker
# from sqlalchemy import URL, create_engine, text
# from config import settings

# sync_engine = create_engine(
#     url =  settings.DATABASE_URL_psycopg,
#     echo = 0
# )

# async_engine = create_async_engine(
#     url =  settings.DATABASE_URL_asyncpg,
#     echo = 0
# )

# with sync_engine.connect() as conn:
#     res = conn.execute(text('SELECT 1,2,3'))
#     print(f'result = {res.all()[0]}')
    
# async def get_123():
#     async with async_engine.connect() as conn:
#         res = await conn.execute(text('SELECT 1,2,3'))
#         print(f'result = {res.all()[0]}')

# asyncio.run(get_123())


#Ex_1
# from sqlalchemy import create_engine, text
# from config import settings
# sync_engine = create_engine(
#     url = settings.DATABASE_URL_psycopg
# )

# with sync_engine.connect() as conn:
#     res = conn.execute(text('SELECT 100, 200, 300'))
#     print(f'resul = {res.first()[0]}')


#Ex_2
# import asyncio
# from sqlalchemy.ext.asyncio import create_async_engine
# from config import settings
# from sqlalchemy import text
# async_engine = create_async_engine(
#     url = settings.DATABASE_URL_asyncpg
# )
 
# async def get_200():
#     async with async_engine.connect() as conn:
#         res = await conn.execute(text('SELECT 100, 200, 300'))
#         print(f'result = {res.first()[1]}')

# asyncio.run(get_200())

#Ex_3
# import asyncio
# from sqlalchemy.ext.asyncio import create_async_engine
# from config import settings
# from sqlalchemy import create_engine, text

# async_engine = create_async_engine(
#     url = settings.DATABASE_URL_asyncpg
# )
 
# async def get_msg():
#     async with async_engine.connect() as conn:
#         res = await conn.execute(text("SELECT 'hello' AS msg"))
#         row = res.mappings().all()[0]
#         print(f'сообщение : {row['msg']}')

# asyncio.run(get_msg())



# sync_engine = create_engine(
#     url = settings.DATABASE_URL_psycopg
# )

# with sync_engine.connect() as conn:
#     res = conn.execute(text("SELECT 'hello' AS msg"))
#     row = res.mappings().all()[0]
#     print(f'сообщение : {row['msg']}')

1    














