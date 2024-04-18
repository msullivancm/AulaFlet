from typing import Optional
from pydantic import BaseModel, validator

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int 

    @validator('titulo')
    def validate_titulo(cls, value):
        if value.islower():
            raise ValueError("O título deve ser capitalizado")
        return value
    
    @validator('aulas')
    def validate_aulas(cls, value):
        if value <= 0:
            raise ValueError("O número de aulas deve ser maior que 0")
        return value
    
    @validator('horas')
    def validate_horas(cls, value):
        if value <= 0:
            raise ValueError("O número de horas deve ser maior que 0")
        return value
    
        
""" cursos = [
    Curso(id=1, titulo="Programação para leigos", aulas=112, horas=58),
    Curso(id=2, titulo="Algoritmos e Lógica de Programação", aulas=87, horas=67),
    Curso(id=3, titulo="Algoritmos e Lógica de Programação 2", aulas=100, horas=70),
    Curso(id=4, titulo="Algoritmos e Lógica de Programação 3", aulas=140, horas=80),
    Curso(id=5, titulo="Algoritmos e Lógica de Programação 4", aulas=150, horas=90),
] """