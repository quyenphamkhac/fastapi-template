from typing import List, Union
from pydantic import BaseModel


class TodoBase(BaseModel):
    name: str
    description: Union[str, None] = None
    tags: List[str] = []


class TodoCreate(TodoBase):
    pass


class Todo(TodoBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class TodoUpdate(TodoBase):
    id: int
