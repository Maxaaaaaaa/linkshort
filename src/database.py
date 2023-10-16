from databases import Database
from .config import settings

database = Database(settings.database_url)

async def connect_to_database():
    await database.connect()

async def close_database_connection():
    await database.disconnect()
