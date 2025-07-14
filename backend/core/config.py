# Used to import environment variables that we will use anywhere in our project
from typing import List
from pydantic_settings import BaseSettings
from pydantic import field_validator

# Everything specified in this class must match what is specified in the .env
# .env file and variables in this must match. If you add any .env variable, you must specify it here.
class Settings(BaseSettings):
    DATABASE_URL: str
    API_PREFIX: str = '/api'
    Debug: bool = False
    ALLOWED_ORIGINS: str = ""
    GOOGLE_API_KEY: str

    # This doesn't support list, but to make ALLOWED_ORIGINS a list, we do:
    @field_validator("ALLOWED_ORIGINS")
    def parse_allowed_origins(v:str):
        return v.split(",") if v else[]
    
    # Class configuration 
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

# Instantiating settings class
settings = Settings()



