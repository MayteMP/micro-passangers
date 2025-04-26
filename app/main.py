from fastapi import FastAPI
from app.database import database, engine, metadata
from app.models import usuarios

app = FastAPI()

# Crear tablas
metadata.create_all(engine)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/passengers")
async def listar_usuarios():
    query = usuarios.select()
    return await database.fetch_all(query)

@app.post("/passengers")
async def crear_usuario(name: str, last_name: str, birthdate: str):
    query = usuarios.insert().values(name=name, last_name=last_name, birthdate=birthdate)
    await database.execute(query)
    return {"message": "Usuario creado exitosamente"}