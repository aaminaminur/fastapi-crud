from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from config.db import meta

banks = Table(
    'bank_master_table', meta,
    Column('master_bank_id', Integer, primary_key=True),
    Column('ifsc_first4', String(4)),
    Column('is_enach_net_active', Boolean),
    Column('is_enach_card_active', Boolean),
    Column('is_enach_esign_active', Boolean),
    Column('is_active', Boolean),
)
