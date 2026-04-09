from fastapi import FastAPI
from database import Database
from models import Base
from schemas import HealthCheck

app = FastAPI()

@app.on_event("startup")
async def startup():
    await Database.connect()

@app.on_event("shutdown")
async def shutdown():
    await Database.disconnect()

@app.get("/health", response_model=HealthCheck)
async def health_check():
    return {"status": "ok"}