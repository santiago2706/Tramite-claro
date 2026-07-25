from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    app_name: str =  "Tramite claro"
    app_env: str = "development"
    app_version: str = "0.1.0"
    host: str = "127.0.0.1"
    port: int = 8000
    log_level: str = "INFO" 
    model_config = SettingsConfigDict(
        env_file = ".even",
        env_file_encoding = "utf-8",
        extra = ignore,
    )
Settings = Settings()