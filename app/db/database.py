from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, Session

db_name = "MiniRestaurant"
db_user = "MiniResUser"
db_pass = "#$MiniResUser"

SQLALCHEMY_DATABASE_URL = f"postgresql://{db_user}:{db_pass}@localhost:5432/{db_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
