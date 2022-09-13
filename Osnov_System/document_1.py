from fastapi import FastAPI, Request
from Poboch_System import document_2
import requests

document_1 = FastAPI()
document_1.mount('/document_2', document_2.document_2)

@document_1.get("/")
def root(request: Request):
    host = request.client.host
    port = 8000 # request.client.port
    url = f"http://{host}:{port}/document_2/"
    res = requests.get(url)
    return res.json()