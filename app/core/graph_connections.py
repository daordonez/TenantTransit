from app.core.graph_client import GraphClient
from app.core.config import settings

#Create connections (It creates the effective communication bridge)
async def initialize_connections():
    #We've got access to settings()
    #Requesting source and target access token, so it's mandatory provide params
    
    #Source
    source_auth = GraphClient(
        clientId=settings.source_clientId,
        clientSecret=settings.source_clientSecret,
        tenantId=settings.source_tenantId
    )
    
    #Target
    target_auth = GraphClient(
        clientId=settings.target_clientId,
        clientSecret=settings.target_clientSecret,
        tenantId=settings.target_tenantId
    )
    
    #request tokens
    try:
        source_token = await source_auth.getToken()
        target_token = await target_auth.getToken()
    finally:
        await source_auth.close()
        await target_auth.close()
        
    return source_token, target_token