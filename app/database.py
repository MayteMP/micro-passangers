import os
from dotenv import load_dotenv
from databases import Database
from sqlalchemy import create_engine, MetaData

# Cargar variables del archivo .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

database = Database(DATABASE_URL)
metadata = MetaData()
engine = create_engine(DATABASE_URL)