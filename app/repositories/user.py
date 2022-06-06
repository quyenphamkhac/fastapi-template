from sqlalchemy.orm import Session
from fastapi import Depends
from app.core.security import hash_password
from app.db.base import get_db
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
        hashed_password = hash_password(user.password)
        db_user = User(email=user.email, hashed_password=hashed_password)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_user_by_email(self, email: str):
        db_user = self.db.query(User).filter(User.email == email).first()
        return db_user
