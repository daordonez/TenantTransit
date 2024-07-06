from azure.identity.aio import ClientSecretCredential # type: ignore
from msgraph import GraphServiceClient # type: ignore

class GraphClient:
    #Creates credential object
    def __init__(self, clientId, clientSecret, tenantId):
        
        self.client_credentials = ClientSecretCredential(
            tenant_id=tenantId,
            client_id=clientId,
            client_secret=clientSecret
        )
        
        #Creates new graph-client
        self.client = GraphServiceClient(self.client_credentials)
    
    async def getToken(self):
        scopes = 'https://graph.microsoft.com/.default'
        #Client contains params to request OAuthToken
        access_token = await self.client_credentials.get_token(scopes)
        return access_token.token
    
    async def close(self):
        await self.client_credentials.close()

