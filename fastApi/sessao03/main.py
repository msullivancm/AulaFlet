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

from typing import Any
from fastapi import Depends, FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi import Path
from fastapi import Query
from fastapi import Header
from models import Curso

from routes import curso_router
from routes import usuario_router

app = FastAPI(
    title = "Aula de FastAPI",
    version = "0.0.1",
    description="Esta é uma API de exemplo criada na aula de FastAPI do Geek University.",
    contact={
        "name": "TIBrasil.net",
        "url": "https://www.tibrasil.net",
        "email": "msullivancm@gmail.com"
    }
)

cursos = {
    1: {"titulo": "Programação para leigos", "aulas": 112, "horas": 58},
    2: {"titulo": "Algoritmos e Lógica de Programação", "aulas": 87, "horas": 67},
    3: {"titulo": "Algoritmos e Lógica de Programação 2", "aulas": 100, "horas": 70},
    4: {"titulo": "Algoritmos e Lógica de Programação 3", "aulas": 140, "horas": 80},
    5: {"titulo": "Algoritmos e Lógica de Programação 4", "aulas": 150, "horas": 90},
}

def fake_db():
    try:
        print('Abrindo banco de dados...')
    finally:
        print('Fechando banco de dados...')

@app.get("/cursos", 
         description="Retorna uma lista de cursos.", 
         response_description="Lista de cursos.", 
         response_model=dict[int, Curso])
async def get_cursos(db: Any = Depends(fake_db)):
    return cursos


@app.get("/cursos/{curso_id}",
         description="Retorna um curso pelo ID.",
         response_description="Curso encontrado",
         response_model=Curso)
async def get_curso(
    curso_id: int = Path(
        title="ID do Curso",
        description="Informe o ID do curso desejado entre 1 e 4.",
        gt=0,
        lt=5,
    ),
    db: Any = Depends(fake_db)
):
    try:
        curso = cursos[curso_id]
        # curso.update({"id": curso_id})
        return curso
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado."
        )


@app.post("/cursos", status_code=status.HTTP_201_CREATED,
          description="Inclui um novo curso.",
         response_description="Curso incluído com sucesso.",
         response_model=Curso)
async def post_curso(curso: Curso, db: Any = Depends(fake_db)):
    next_id: int = len(cursos) + 1
    if curso.titulo not in cursos:
        # exclui o atributo id do curso que, somente lá na frente será gerado por autonumeração do banco de dados. neste momento não é necessário.
        del curso.id
        cursos[next_id] = curso
        return curso
    else:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Já existe o curso com ID {curso.id}.",
        )


@app.put("/cursos/{curso_id}",
         description="Atualiza um curso pelo ID.",
         response_description="Curso atualizado com sucesso.",
         response_model=Curso)
async def put_curso(curso_id: int, curso: Curso, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        cursos[curso_id] = curso
        return curso
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Registro não encontrado."
        )


@app.delete("/cursos/{curso_id}", status_code=status.HTTP_204_NO_CONTENT,
            description="Exclui um curso pelo ID.",
            response_description="Curso excluído com sucesso.")
async def delete_curso(curso_id: int, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        del cursos[curso_id]
        return {"message": "Curso excluído com sucesso."}
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Registro não encontrado."
        )

@app.get('/calculadora', description="Calculadora simples.", response_description="Resultado da operação.")
async def calculadora(x: float, sinal: str, y: float, x_geek: str = Header(None, description='Header X-Geek', example='Geek University')):
    if sinal in ['+', '-', '*', '/']:
        if sinal == '+':
            resultado = x + y
        elif sinal == '-':
            resultado = x - y
        elif sinal == '*' or sinal.lower() == 'x':
            resultado = x * y
        elif sinal == '/':
            resultado = x / y
        return {"resultado": resultado, "x_geek": x_geek}
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Operação inválida."
        )

#incluindo as rotas dos routers
app.include_router(curso_router.router, tags=['cursos'])
app.include_router(usuario_router.router, tags=['usuarios'])

        
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000)
