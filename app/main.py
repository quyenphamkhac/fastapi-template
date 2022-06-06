from sys import prefix
from fastapi import FastAPI
from app.routers import router
from app.db.base import engine
from app.models import Base
from starlette.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)


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
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )
    app.include_router(router, prefix='')
    return app


app = get_app()
