from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # AWS Credentials
    aws_access_key_id: str
    aws_secret_access_key: str
    aws_region: str
    sqs_queue_url: str
    
    # WhatsApp Config
    whatsapp_verify_token: str
    
    # App Config
    app_name: str = "WhatsApp Webhook"
    debug: bool = False
    
    class Config:
        env_file = ".env"
        # Converte automaticamente os nomes das variáveis
        # ex: aws_access_key_id -> AWS_ACCESS_KEY_ID
        case_sensitive = False

@lru_cache()
def get_settings() -> Settings:
    return Settings() 