from azure.identity.aio import ClientSecretCredential
from msgraph import GraphServiceClient

class GraphClient:
    
    
    #Creates credential object
    def __init__(self, clientId, clientSecret, tenantId):
        
        self.credentials = ClientSecretCredential(
            tenant_id=tenantId,
            client_id=clientId,
            client_secret=clientSecret
        )
        
        #Creates new graph-client
        self.client = GraphServiceClient(self.credentials)
    
    async def getToken(self):
        self.scopes = ['https://graph.microsoft.com/.default']
        access_token = self.credentials.get_token(self.scopes)
        return access_token
        