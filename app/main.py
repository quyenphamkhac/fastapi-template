from fastapi import FastAPI
from app.routers.todos import router as todos_router
from app.db.database import engine, SessionLocal, Base


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
    return app


app = get_app()
