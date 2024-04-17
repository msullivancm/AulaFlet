#pip install fastapi 
#pip install uvicorn
#pip freeze > requirements.txt

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def raiz():
    return {"msg": "FastAPI"}