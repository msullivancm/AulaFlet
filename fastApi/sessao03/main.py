"""
pip install fastapi 
pip install uvicorn
pip install fastapi2postman
pip freeze > requirements.txt

#para gerar arquivo de importação da api completa para o postman
fastapi2postman --app nomedoarquivosemopontopy:app --output sessao03.json
##caso o nome do arquivo seja main.py não precisa especificar o app
fastapi2postman --app main --output sessao03.json
"""

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from models import Curso

app = FastAPI()

cursos = {
    1: {
        "titulo": "Programação para leigos",
        "aulas": 112,
        "horas": 58
    },
    2: {
        "titulo": "Algoritmos e Lógica de Programação",
        "aulas": 87,
        "horas": 67
    }
}

@app.get('/cursos')
async def get_cursos():
    return cursos

@app.get('/cursos/{curso_id}')
async def get_curso(curso_id: int):
    try: 
        curso = cursos[curso_id]
        #curso.update({"id": curso_id})
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado.')

@app.post('/cursos')
async def post_curso(curso: Curso):
    next_id: int = len(cursos) + 1
    if curso.titulo not in cursos:
        #exclui o atributo id do curso que, somente lá na frente será gerado por autonumeração do banco de dados. neste momento não é necessário.
        del curso.id
        cursos[next_id] = curso
        return curso
    else: 
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f'Já existe o curso com ID {curso.id}.')

if __name__ == '__main__':
    import uvicorn 
    uvicorn.run("main:app", host="0.0.0.0", port=8000)