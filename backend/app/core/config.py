from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    #connexion postgresql
      DATABASE_URL:str
      #securite JWT 
      SECRET_Key:str
      ACCESS_TOKEN_EXPIRE_MINUTES:int
      ALGORITHM:str
      
      #conf inter
      model_config=SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )
settings=Settings()
