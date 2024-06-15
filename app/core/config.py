from pydantic import BaseSettings

class Settings(BaseSettings):
    # source
    source_clientId: str
    source_clientSecret: str
    target_tenantId: str
    #target
    target_clientId: str
    target_clientSecret: str
    target_tenantId: str
    
    class Config:
        env_file = ".env"
        
settings = Settings()