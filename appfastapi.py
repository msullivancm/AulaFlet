import flet as ft
import flet_fastapi

from contextlib import asynccontextmanager

from fastapi import FastAPI
import requests
import asyncio
from concurrent.futures import ThreadPoolExecutor

@asynccontextmanager
async def lifespan(app: FastAPI):
    await flet_fastapi.app_manager.start()
    yield
    await flet_fastapi.app_manager.shutdown()

async def fetch_data(url: str):
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as pool:
        data = await loop.run_in_executor(pool, lambda: requests.get(url).json())
    return data

app = FastAPI(lifespan=lifespan)

@app.get('/user/{id}')
async def get_user(id: int):
    return {'user': f'Buscando os dados do usuário de ID: {id}'}

async def main(page: ft.Page):
    await page.add_async(ft.Text('Meu App Flet'))

    data = await fetch_data('http://127.0.0.1:8080/user/1')
    await page.add_async(ft.Text(data['user']))

app.mount(path='/',app=flet_fastapi.app(main))

###Iniciando o server fastapi
#uvicorn appfastapi:app --port 8080 --reload
#documentação em swagger: http://127.0.0.1:8080/docs