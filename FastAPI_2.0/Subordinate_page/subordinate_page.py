from fastapi import FastAPI
import uvicorn
import os

subordinate_page = FastAPI()

@subordinate_page.get('/')
def root():
    return {'datakey':'necontent'}


@subordinate_page.get("/get_data")
def get_data():
    return {'datakey':'hello comp'}

if __name__ == '__main__':
    uvicorn.run('subordinate_page:subordinate_page',host='0.0.0.0',port=80,reload=True)