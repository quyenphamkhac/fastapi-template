# Import all the models, so that Base has them before being
# imported by Alembic
from app.models.base import Base
from app.models.item import Item
from app.models.todo import Todo
from app.models.user import User
