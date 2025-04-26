from fastapi import FastAPI, Request, HTTPException
from config.database import database, engine, metadata
from app.models import passengers
from datetime import datetime
from contextlib import asynccontextmanager

metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
  await database.connect()
  yield
  await database.disconnect()

app = FastAPI(lifespan=lifespan)

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

  query = passengers.insert().values(name=name, last_name=last_name, birthdate=parse_date(birthdate))

  try:
    new_id = await database.execute(query)
    return {"id": new_id, "name": name, "last_name": last_name, "birthdate": birthdate}
  except Exception as e:
    raise HTTPException(status_code=400, detail="Passenger register was not created")

def parse_date(str):
  return datetime.strptime(str, '%Y-%m-%d').date()