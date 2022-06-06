from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, ARRAY
from sqlalchemy.orm import relationship
from app.models.base import Base


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    tags = Column(ARRAY(String))
    completed = Column(Boolean)
    new_field = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="todos")
