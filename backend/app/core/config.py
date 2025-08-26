from pydantic import BaseSettings
from dotenv import load_dotenv
import os
        
load_dotenv() # .env dosyasındaki değişkenleri yükler
        
class Settings(BaseSettings):
    SUPABASE_URL: str = os.getenv("SUPABASE_URL", "")
    SUPABASE_SERVICE_KEY: str = os.getenv("SUPABASE_SERVICE_KEY", "")
    TMDB_API_KEY: str = os.getenv("TMDB_API_KEY", "")
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
        
    class Config:
        case_sensitive = True
        
settings = Settings()

