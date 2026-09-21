from pydantic import BaseModel, Field
from typing import Optional

class Editorial(BaseModel):
    idEd: int = Field(
        ..., gt=0, description="Identificador único de la editorial")
    nombre: str = Field(
        ..., min_length=1, max_length=100)
    pais: str = Field(
        ..., min_length=1, max_length=50)

class Libro(BaseModel):
    isbn: str = Field(
        ..., min_length=10, max_length=13, description="Código ISBN")
    titulo: str = Field(
        ..., min_length=1, max_length=100)
    autor: str = Field(
        ..., min_length=1, max_length=50)
    precio: float = Field(
        ..., gt=0.0, description="Precio del libro")
    editorial: Optional[Editorial] = None
