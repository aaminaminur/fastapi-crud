from fastapi import APIRouter
from config.db import conn, meta
from model.index import banks
from schemas.index import Bank
from sqlalchemy import update

bankmaster = APIRouter()


@bankmaster.get("/banks_list/")
async def get_banks_list():
    return conn.execute(banks.select()).fetchall()


@bankmaster.post("/add_bank/")
async def add_bank(bank: Bank):
    conn.execute(banks.insert().values(
        ifsc_first4=bank.ifsc_first4,
        is_enach_net_active=bank.is_enach_net_active,
        is_enach_card_active=bank.is_enach_card_active,
        is_enach_esign_active=bank.is_enach_esign_active,
        is_active=bank.is_active
    ))
    return conn.execute(banks.select()).fetchall()


@bankmaster.put("/modify_bank/")
async def modify_bank(data: dict, master_bank_id: int):
    update_table = update(meta.tables['bank_master_table'])
    conn.execute(update_table.values(data).where(banks.c.master_bank_id==master_bank_id))
    return conn.execute(banks.select()).fetchall()


@bankmaster.delete("/{master_bank_id}")
async def delete_data(master_bank_id: int):
    conn.execute(banks.delete().where(banks.c.master_bank_id == master_bank_id))
    return conn.execute(banks.select()).fetchall()
