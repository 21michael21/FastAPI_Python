from fastapi import FastAPI
import requests
import host_configuration

Osnova_page = FastAPI()

@Osnova_page.get("/")
def get_data():
    url =  f'http://{host_configuration.another_host}:{host_configuration.another_port}'
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()
    else:
        return {'error':'xxxx'}

@Osnova_page.get("/another api/{api_request}")
def get_data(api_request : str):
    url =  f'http://{host_configuration.another_host}:{host_configuration.another_port}/{api_request}'
    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else:
        return {'error':'xxxx'}