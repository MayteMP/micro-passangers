import os
from dotenv import load_dotenv
from databases import Database
from sqlalchemy import create_engine, MetaData

ENV = os.getenv("ENV", "dev")
env_file = ".env.test" if ENV == "test" else ".env"
load_dotenv(env_file)
DATABASE_URL = os.getenv("DATABASE_URL")

metadata = MetaData()
database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {})
