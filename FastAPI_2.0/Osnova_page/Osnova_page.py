from fastapi import FastAPI
import requests
import os
import uvicorn



osnova_page = FastAPI()

@osnova_page.get("/")
def get_data():
	return {'type':'content'}
@osnova_page.get("/get_data")
def get_data():
    url = f'{os.getenv(key="URL")}/get_data'
    try:
        result = requests.get(url)
        if result.status_code == 200:
            return result.json()
        else:
            return {'error':'xxxx'}
    except Exception as ex:
        result = {'error':ex, 'url':url,'url2':os.getenv(key="URL")}
        return result

if __name__ == '__main__':
   uvicorn.run('osnova_page:osnova_page',host='0.0.0.0',port=80,reload=True)
  #   url =  f'http://{host_configuration.another_host}:{host_configuration.another_port}'
  #  res = requests.get(url)
  #  if res.status_code == 200:
  #      return res.json()
  #  else:
  #      return {'error':'xxxx'}

# @osnova_page.get("/another api/{api_request}")
# def get_data(api_request : str):
#     url =  f'http://{host_configuration.another_host}:{host_configuration.another_port}/{api_request}'
#     result = requests.get(url)
#     if result.status_code == 200:
#         return result.json()
#     else:
#         return {'error':'xxxx'}
