from fastapi import Depends
from fastapi.security import HTTPBearer
from app.core.security import verify_password
from app.repositories.user import UserRepository
import app.schemas.user_schema as schemas


class UserService(object):
    __instance = None

    reusable_oauth2 = HTTPBearer(
        scheme_name="Authorization",
    )

    def __init__(self, repo: UserRepository = Depends(UserRepository)) -> None:
        self.repo = repo

    def authenticate(self, auth_data: schemas.UserLogin) -> schemas.User:
        user = self.repo.get_user_by_email(auth_data.email)
        if not user:
            return None
        if not verify_password(auth_data.password, user.hashed_password):
            return None
        return user

    def create_user(self, user: schemas.UserCreate) -> schemas.User:
        user = self.repo.create_user(user)
        return user
