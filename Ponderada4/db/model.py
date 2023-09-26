import psycopg2
from dotenv import load_dotenv
from os import environ

load_dotenv()

conn = psycopg2.connect(
    host=str(environ.get("POSTGRES_HOST")),
    database=str(environ.get("POSTGRES_DB")),
    user=str(environ.get("POSTGRES_USER")),
    password=str(environ.get("POSTGRES_PASSWORD"))
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS predictions (
    id SERIAL PRIMARY KEY,
    prediction TEXT NOT NULL
);

""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
""")

conn.commit()

conn.close()