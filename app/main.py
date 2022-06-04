from fastapi import FastAPI
from app.routers.todos import router as todos_router
from app.routers.users import router as users_router
from app.db.database import engine, Base
import app.models.todo
import app.models.user
import app.models.item

Base.metadata.create_all(bind=engine)

print(Base.metadata)


def get_app():
    app = FastAPI(
        title='Lisence OCR Project',
        docs_url='/docs',
        redoc_url='/redoc',
        openapi_url='/openapi.json',
        description='''
        This is a simple API for OCR project.
        '''
    )
    app.include_router(todos_router, prefix="/api/todos")
    app.include_router(users_router, prefix="/api/users")
    return app


app = get_app()
