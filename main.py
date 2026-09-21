from fastapi import FastAPI, HTTPException
from models import Libro, Editorial

app = FastAPI(title="API Biblioteca")

editoriales_db = {
    1: Editorial(idEd=1, nombre="Alfaomega", pais="México"),
    2: Editorial(idEd=2, nombre="O'Reilly Media", pais="Estados Unidos")
}

libros_db = {
    "9780135957059": Libro(
        isbn="9780135957059",
        titulo="Pragmatic Programmer",
        autor="Andrew Hunt",
        precio=45.99,
        editorial=editoriales_db[1]
    ),
    "9781491957660": Libro(
        isbn="9781491957660",
        titulo="Fluent Python",
        autor="Luciano Ramalho",
        precio=59.99,
        editorial=editoriales_db[2]
    )
}

@app.get("/")
def home():
    return {"mensaje": "API Biblioteca activa"}

@app.get("/books/{isbn}", response_model=Libro)
def get_book(isbn: str):
    if isbn not in libros_db:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return libros_db[isbn]

@app.get("/editoriales/{id_ed}", response_model=Editorial)
def get_editorial(id_ed: int):
    if id_ed not in editoriales_db:
        raise HTTPException(status_code=404, detail="Editorial no encontrada")
    return editoriales_db[id_ed]
