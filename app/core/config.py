from pydantic_settings import BaseSettings, SettingsConfigDict
import os

DOTENV = os.path.join(os.path.dirname(__file__),".env")
class Settings(BaseSettings):
    
    
    # source
    source_clientId: str
    source_clientSecret: str
    source_tenantId: str
    #target
    target_clientId: str
    target_clientSecret: str
    target_tenantId: str
    
    model_config = SettingsConfigDict(env_file=DOTENV)

settings = Settings()