import re
from fastapi import APIRouter
from app.schemas.todo_schema import Todo
from app.schemas.common import ResponseModel

router = APIRouter()


@router.get("/", dependencies=[], tags=["todos"], response_model=ResponseModel)
async def get_todos():
    return ResponseModel().return_with_code(200, "Todos list", [])


@router.post("/", dependencies=[], tags=["todos"], response_model=ResponseModel)
async def create_todo(todo: Todo):
    return {"todo": todo}


@router.get("/{todo_id}", dependencies=[], tags=["todos"], response_model=ResponseModel)
async def get_todo(todo_id: int):
    return {"todo": {"name": "test", "description": "test"}}


@router.put("/{todo_id}", dependencies=[], tags=["todos"], response_model=ResponseModel)
async def update_todo(todo_id: int, todo: Todo):
    return {"todo": todo}


@router.delete("/{todo_id}", dependencies=[], tags=["todos"], response_model=ResponseModel)
async def delete_todo(todo_id: int):
    return {"todo": {"name": "test", "description": "test"}}
