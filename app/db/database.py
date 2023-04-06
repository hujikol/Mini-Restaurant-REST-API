from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_name = "MiniRestaurant"
db_user = "MiniResUser"
db_pass = "#$MiniResUser"

SQLALCHEMY_DATABASE_URL = "postgresql://{}:{}@localhost:5432/{}".format(db_user, db_pass, db_name)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()