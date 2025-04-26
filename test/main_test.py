import os
os.environ["ENV"] = "test"
import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app
import aiosqlite
from config.database import database, engine, metadata

@pytest.fixture(autouse=True, scope="module")
async def setup_and_teardown():
  metadata.create_all(engine)
  await database.connect()
  yield
  await database.disconnect()

@pytest.mark.asyncio
async def test_create_passenger():
  transport = ASGITransport(app)
  async with AsyncClient(transport=transport, base_url="http://test") as ac:
    payload = {
      "name": "Jeronimo",
      "last_name": "Arango",
      "birthdate": "2000-03-12"
    }
    response = await ac.post("/passengers", json=payload)

  assert response.status_code == 200
  data = response.json()
  assert data["name"] == "Jeronimo"
  assert data["last_name"] == "Arango"
  assert data["birthdate"] == "2000-03-12"
  assert "id" in data
