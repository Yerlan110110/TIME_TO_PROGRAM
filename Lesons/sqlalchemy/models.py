from sqlalchemy import Table, Column , Integer, String, MetaData
metadata = MetaData()

wokers_table = Table(
    'workers', metadata,
    Column('id', Integer, primary_key=True),
    Column('Username', String)
)