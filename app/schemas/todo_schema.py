from typing import List, Union
from pydantic import BaseModel


class Todo(BaseModel):
    name: str
    description: Union[str, None] = None
    tags: List[str] = []
