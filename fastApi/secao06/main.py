"""
pip install fastapi 
pip install uvicorn
pip install fastapi2postman
pip freeze > requirements.txt

#para gerar arquivo de importação da api completa para o postman
fastapi2postman --app nomedoarquivosemopontopy:app --output secao3.json
##caso o nome do arquivo seja main.py não precisa especificar o app
fastapi2postman --app main --output secao06.json
"""

from fastapi import FastAPI

from core.configs import settings
from api.v1.api import api_router


app = FastAPI(title='Curso API - Segurança')
app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000,
                log_level='info', reload=True)


"""
Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNzE0MDcyMDA2LCJpYXQiOjE3MTM0NjcyMDYsInN1YiI6IjEifQ.9knHTmLyH5ImKCSjgt6m02dPOL4RarBNVushX1uT0Cs
Tipo: bearer
"""
