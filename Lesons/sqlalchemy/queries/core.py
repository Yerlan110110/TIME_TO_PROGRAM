from database import sync_engine, async_engine
from sqlalchemy import text, insert
from models import metadata_obj, workers_table

def get_123_sync():
    with sync_engine.connect as conn:
        res = conn.execute(text('SELECT 1,2,3'))
        print(res.all())


def get_123_async():
    with async_engine as conn:
        res = conn.execute(text('SELECT 1, 2, 3'))
        print(res.all())


def create_tables():
    metadata_obj.drop_all(sync_engine)
    metadata_obj.create_all(sync_engine)


def insert_data():
    with sync_engine.connect() as conn:
        stmt = insert(workers_table).values(
            [
                {'username': 'Bobr'},
                {'username': 'Kurva'},
            ]
        )
        conn.execute(stmt)
        conn.commit()
        