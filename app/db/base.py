from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


POSTGRESQL_DATABASE_URL = "postgresql+pg8000://postgres:postgres@localhost/todo"

engine = create_engine(POSTGRESQL_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
