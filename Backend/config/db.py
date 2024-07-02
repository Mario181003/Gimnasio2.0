from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEM_DATABASE_URL="mysql+pymysql://root:1234@localhost:3307/test.db"

engine = create_engine(SQLALCHEM_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)
Base = declarative_base()