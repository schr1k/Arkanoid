import psycopg2

from config import *


class DB:
    def __init__(self):
        self.connection = None

    def connect(self):
        self.connection = psycopg2.connect(
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
            host=POSTGRES_HOST,
            port=POSTGRES_PORT,
            dbname=POSTGRES_DB
        )
        self.connection.autocommit = True

    def insert_new_record(self, name: str, points: int):
        cursor = self.connection.cursor()
        cursor.execute(
            'INSERT INTO users (name, points) VALUES (%s, %s)', (name, points,)
        )

    def get_top(self) -> list[tuple]:
        cursor = self.connection.cursor()
        cursor.execute(
            'SELECT name, points FROM users ORDER BY points DESC LIMIT 10'
        )
        result = cursor.fetchall()
        return result
