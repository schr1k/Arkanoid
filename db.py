import asyncpg

from config import *


class DB:
    def __init__(self):
        self.connection = None

    async def connect(self):
        self.connection = await asyncpg.connect(
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
            host=POSTGRES_HOST,
            port=POSTGRES_PORT,
            database=POSTGRES_DB
        )

    # SELECT ===========================================================================================================
    async def insert_new_record(self, name: str, points: int):
        await self.connection.execute(
            'INSERT INTO users (name, points) VALUES ($1, $2)', name, points
        )

    async def get_top(self) -> list:
        result = await self.connection.fetch(
            'SELECT name, points FROM users ORDER BY points DESC LIMIT 10'
        )
        return [dict(i) for i in result]
