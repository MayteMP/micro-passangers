from fastapi import FastAPI, Request, HTTPException
from app.database import database, engine, metadata
from app.models import passengers
from datetime import datetime
# remove after test
import pdb

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
async def list_passengers():
  query = passengers.select()
  return await database.fetch_all(query)

@app.post("/passengers")
async def create_pasessenger(request: Request):
  data = await request.json()
  name = data.get("name")
  last_name = data.get("last_name")
  birthdate = data.get("birthdate")

  if not name or not last_name or not birthdate:
    raise HTTPException(status_code=400, detail="Faltan campos obligatorios")

  query = passengers.insert().values(name=name, last_name=last_name, birthdate=datetime.strptime(birthdate, '%Y-%m-%d').date())

  try:
    new_id = await database.execute(query)
    return {"id": new_id, "name": name, "last_name": last_name, "birthdate": birthdate}
  except Exception:
    pdb.set_trace()
    raise HTTPException(status_code=400, detail="Passenger register was not created")
