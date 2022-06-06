from fastapi import APIRouter, Depends, HTTPException
from app.core.security import generate_jwt_token
from app.schemas.jwt_schema import JwtToken
import app.schemas.user_schema as user_schema
from app.services.user_svc import UserService
from app.schemas.common import ResponseModel


router = APIRouter()


@router.post("/login", dependencies=[], tags=["auth"], response_model=ResponseModel[JwtToken])
async def login(data: user_schema.UserLogin, user_svc: UserService = Depends(UserService)):
    user = user_svc.authenticate(data)
    if not user:
        raise HTTPException(
            status_code=400, detail='Incorrect email or password')
    access_token = generate_jwt_token(data={"user_id": user.id})
    return ResponseModel().return_success({
        'access_token': access_token
    })
