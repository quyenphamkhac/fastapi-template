
from fastapi import APIRouter, Depends
import app.schemas.user_schema as schemas
from app.services.user_svc import UserService

router = APIRouter()


@router.post("/", dependencies=[], tags=["users"], response_model=schemas.User)
async def create_user(data: schemas.UserCreate, svc: UserService = Depends(UserService)):
    return svc.create_user(data)
