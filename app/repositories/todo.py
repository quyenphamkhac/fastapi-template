from sqlalchemy.orm import Session
from fastapi import Depends
from app.db.database import get_db
from app.models.todo import Todo
import app.schemas.todo_schema as schemas


def get_todo_repository():
    return TodoRepository()


class TodoRepository(object):
    __instance__ = None

    def __init__(self, db: Session = Depends(get_db)) -> None:
        self.db = db

    def get_todo(self, todo_id: int):
        return self.db.query(Todo).filter(Todo.id == todo_id).first()

    def get_todos(self, skip: int = 0, limit: int = 100):
        return self.db.query(Todo).offset(skip).limit(limit).all()

    def create_todo(self, todo: schemas.TodoCreate, user_id: int):
        db_todo = Todo(**todo.dict(), owner_id=user_id)
        self.db.add(db_todo)
        self.db.commit()
        self.db.refresh(db_todo)
        return db_todo
