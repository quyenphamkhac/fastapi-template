import jwt
from fastapi.security import HTTPBearer
from datetime import datetime, timedelta
from app.core.config import settings

reusable_oauth2 = HTTPBearer(scheme_name="Authorization")


def generate_jwt_token(*, data: dict, expires_delta: int = settings.ACCESS_TOKEN_EXPIRE_SECONDS):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + timedelta(seconds=expires_delta)
        to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.SECURITY_ALGORITHM)
    return encoded_jwt


def verify_jwt_token(token: str):
    decoded_jwt = jwt.decode(token,  settings.SECRET_KEY, algorithms=[
                             settings.SECURITY_ALGORITHM])
    return decoded_jwt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return hashed_password == plain_password


def hash_password(plain_password: str) -> str:
    return plain_password
