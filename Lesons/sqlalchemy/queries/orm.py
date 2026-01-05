from database import sync_engine, async_engine,session_factory, async_session_factory
from sqlalchemy import text, insert
from models import metadata_obj, WorkersOrm


def create_tables():
    metadata_obj.drop_all(sync_engine)
    metadata_obj.create_all(sync_engine)

def insert_data():
    with session_factory as session:
        worker_bobr = WorkersOrm(username = 'Bobr')
        worker_volk = WorkersOrm(username = 'Volk')
        session.add_all([worker_bobr,worker_volk])
        session.commit()


async def insert_data():
    async with async_session_factory() as session:
            worker_bobr = WorkersOrm(username = 'Bobr')
            worker_volk = WorkersOrm(username = 'Volk')
            session.add_all([worker_bobr,worker_volk])
            await session.commit()


