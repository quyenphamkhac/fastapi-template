from webbrowser import get
from sqlalchemy.orm import Session
from fastapi import Depends
from app.repositories.user import UserRepository
import app.schemas.user_schema as schemas


class UserService(object):
    __instance = None

    def __init__(self, repo: UserRepository = Depends(UserRepository)) -> None:
        self.repo = repo
        pass

    def create_user(self, user: schemas.UserCreate) -> schemas.User:
        user = self.repo.create_user(user)
        return user
