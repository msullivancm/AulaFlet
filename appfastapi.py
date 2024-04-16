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

app = FastAPI(lifespan=lifespan)

@app.get('/user/{id}')
async def get_user(id: int):
    return {'user': f'Buscando os dados do usuário de ID: {id}'}