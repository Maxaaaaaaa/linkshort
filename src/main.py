from fastapi import FastAPI
from .database import connect_to_database, close_database_connection
from .link_shortener.routers.link_router import router as link_router

app = FastAPI()

@app.on_event("startup")
async def startup_db():
    await connect_to_database()

@app.on_event("shutdown")
async def shutdown_db():
    await close_database_connection()

app.include_router(link_router)
