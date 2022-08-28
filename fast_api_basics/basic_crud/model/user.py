from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from config.db import meta

users = Table(
    'user_table', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(255)),
    Column('phone', Integer),
    Column('is_test', Boolean),
)
