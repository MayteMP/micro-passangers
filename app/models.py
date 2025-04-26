from sqlalchemy import Table, Column, Integer, String
from app.database import metadata

usuarios = Table(
    "passengers",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(100)),
    Column("last_name", String(100)),
    Column("birthdate", String(100))
)
