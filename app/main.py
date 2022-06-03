from fastapi import FastAPI
from easyocr import Readerclear

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
