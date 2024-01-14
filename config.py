import os

from dotenv import load_dotenv

load_dotenv()

# Postgres
POSTGRES_USER = str(os.getenv('POSTGRES_USER'))
POSTGRES_PASSWORD = str(os.getenv('POSTGRES_PASSWORD'))
POSTGRES_DB = str(os.getenv('POSTGRES_DB'))
POSTGRES_HOST = str(os.getenv('POSTGRES_HOST'))
POSTGRES_PORT = str(os.getenv('POSTGRES_PORT'))
