from sqlalchemy import Column, Integer, String, Boolean, ARRAY
from app.db.database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    tags = Column(ARRAY(String))
    completed = Column(Boolean)
    new_field = Column(String)
