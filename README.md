# micro-passangers
Microservice for see passangers information and update it

# Dependencies
install:

```
pip install fastapi uvicorn sqlalchemy asyncpg databases psycopg2-binary python-dotenv pytest httpx pytest-asyncio aiosqlite
```

# Database

Generate database:

```sql
create database "passenger_db" owner "user";
create table passengers( id serial primary key, name varchar not null, last_name varchar not null, birthdate date not null);
```
