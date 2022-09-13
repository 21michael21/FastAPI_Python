
from fastapi import FastAPI

document_2 = FastAPI()

@document_2.get("/")
def get_data():
    return {"data": "content"}