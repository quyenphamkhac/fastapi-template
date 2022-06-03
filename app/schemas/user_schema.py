from typing import List, Union
from pydantic import BaseModel
from .todo_schema import Todo


class UserBase(BaseModel):
    email: str = None


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool = True
    todos: List[Todo] = []

    class Config:
        orm_mode = True


class UserUpdate(UserBase):
    id: int
