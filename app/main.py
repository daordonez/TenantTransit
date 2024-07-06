from fastapi import FastAPI
from app.api.endpoints import status
from app.core.graph_connections import initialize_connections

# Create an instance of the FastAPI

app = FastAPI()

app.include_router(status.router, prefix="/status", tags=["status"])

@app.on_event("startup")
async def on_startup():
    await initialize_connections()

@app.get("/")
async def read_root():
    return {"message": "Welcome to TenantTransit!"}