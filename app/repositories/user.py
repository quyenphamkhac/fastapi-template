from sqlalchemy.orm import Session
from fastapi import Depends
from app.db.database import get_db
from app.models.user import User
import app.schemas.user_schema as schemas


def get_user_repository():
    return UserRepository()


class UserRepository(object):
    __instance__ = None

    def __init__(self, db: Session = Depends(get_db)) -> None:
        self.db = db
        pass

    def create_user(self, user: schemas.UserCreate):
        hashed_password = user.password + 'the-salt'
        db_user = User(email=user.email, hashed_password=hashed_password)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
