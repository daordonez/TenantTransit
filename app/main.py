from fastapi import FastAPI, HTTPException
from app.api.endpoints import status
from app.core.graph_connections import initialize_connections
from app.db.session import init_db
import logging

#configuring loggin
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create an instance of the FastAPI
app = FastAPI()

app.include_router(status.router, prefix="/status", tags=["status"])

@app.on_event("startup")
async def on_startup():
    #Initialize Database
    try:
        init_db()
        logger.info("Database initialized succesfully.")
    except Exception as e:
        logger.error(f"Failed to initialize database: {e}")
        raise HTTPException(status_code=500, detail="Failed to initialize database")
    
    #Initialize MS Graph connections
    try:
        await initialize_connections()
        logger.info("Micrsoft Graph connections initialized successfully.")
    except Exception as e:
        logger.error(f"Failed to initialize Microsft Graph connections: {e}")
        raise HTTPException(status_code=500, detail="Failed to initialize Microsoft Graph connections")

@app.get("/")
async def read_root():
    return {"message": "Welcome to TenantTransit!"}