from fastapi import APIRouter, HTTPException
from app.core.graph_connections import initialize_connections


router = APIRouter()

@router.get("/")
async def get_connection_status():
    try:
        source_token, target_token = await initialize_connections()
        return{
            "source_tenant_connection":"Successful",
            "source_token": source_token,
            "target_tenant_connection": "successful",
            "target_token": target_token
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))