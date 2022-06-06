from pydantic import BaseModel
from typing import Optional


class JwtToken(BaseModel):
    access_token: str
    token_type: str = 'bearer'


class JwtTokenPayload(BaseModel):
    user_id: Optional[int] = None
