from fastapi import FastAPI
from app.routes import heroes  
from app.database.connection import init_db
from app.routes import admin, auth

app = FastAPI()

@app.get("/")
async def welcome():
    """Welcome message for the Superhero Mission Manager API"""
    return {
        "message": "Welcome to the Superhero Mission Manager API!",
        "documentation": "/docs",
        "endpoints": {
            "heroes": "/api/heroes",
            "missions": "/api/heroes/missions",
            "admin": "/api/admin"
        }
    }

app.include_router(auth.router, prefix="/api") 
app.include_router(admin.router, prefix="/api")
app.include_router(heroes.router, prefix="/api") 

@app.on_event("startup")
async def startup():
    await init_db()