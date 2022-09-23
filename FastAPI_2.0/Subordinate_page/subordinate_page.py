from fastapi import FastAPI

subordinate_page = FastAPI()

@subordinate_page.get('/')
def root():
    return {'datakey':'necontent'}


@subordinate_page.get("/get_data")
def get_data():
    return {'datakey':'content'}