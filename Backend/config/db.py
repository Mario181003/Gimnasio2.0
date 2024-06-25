from sqlalchemy import created_engine, MetaData

engine = created_engine("mysql+pymysql://root:1234@localhost:3307/test.db")

meta = MetaData()

conn = engine.connect()