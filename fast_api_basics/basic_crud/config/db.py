from sqlalchemy import create_engine, MetaData

# engine = create_engine("mysql+pymysql://root:vouch123@localhost/bank_specs")
engine = create_engine("mysql+pymysql://root:vouch123@localhost:3308/test_user")
meta = MetaData()
conn = engine.connect()


# import pandas as pd
# from sqlalchemy import create_engine
#
# cnx = create_engine("mysql+pymysql://root:vouch123@localhost:3308/test_user")
# df = pd.read_sql('SELECT * FROM user_table', cnx)
#
# print(df)
