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
from fastapi import Path
from models import Curso

app = FastAPI()
app.title = "Aula de FastAPI"

cursos = {
    1: {"titulo": "Programação para leigos", "aulas": 112, "horas": 58},
    2: {"titulo": "Algoritmos e Lógica de Programação", "aulas": 87, "horas": 67},
    3: {"titulo": "Algoritmos e Lógica de Programação 2", "aulas": 100, "horas": 70},
    4: {"titulo": "Algoritmos e Lógica de Programação 3", "aulas": 140, "horas": 80},
    5: {"titulo": "Algoritmos e Lógica de Programação 4", "aulas": 150, "horas": 90},
}


@app.get("/cursos")
async def get_cursos():
    return cursos


@app.get("/cursos/{curso_id}")
async def get_curso(
    curso_id: int = Path(
        title="ID do Curso",
        description="Informe o ID do curso desejado entre 1 e 4.",
        gt=0,
        lt=5,
    )
):
    try:
        curso = cursos[curso_id]
        # curso.update({"id": curso_id})
        return curso
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado."
        )


@app.post("/cursos", status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
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


@app.put("/cursos/{curso_id}")
async def put_curso(curso_id: int, curso: Curso):
    if curso_id in cursos:
        cursos[curso_id] = curso
        return curso
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Registro não encontrado."
        )


@app.delete("/cursos/{curso_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_curso(curso_id: int):
    if curso_id in cursos:
        del cursos[curso_id]
        return {"message": "Curso excluído com sucesso."}
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Registro não encontrado."
        )


@app.get('/calculadora')
async def calculadora(a: int,b: int,c: int):
    resultado = a + b + c
    return {"resultado": resultado}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000)
