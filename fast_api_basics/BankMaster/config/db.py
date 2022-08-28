from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:vouch123@localhost:3308/bank_master")
meta = MetaData()
conn = engine.connect()
