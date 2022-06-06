from fastapi import APIRouter
from app.routers import todos, users

router = APIRouter()

router.include_router(todos.router, prefix="/api/todos", tags=["todos"])
router.include_router(users.router, prefix="/api/users", tags=["users"])
