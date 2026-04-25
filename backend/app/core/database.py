from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from app.core.config import settings

#creation engine 
engine=create_engine(settings.DATABASE_URL)

#creation sessionLocal
SessionLocal=sessionmaker(
    autoflush=False, 
    autocommit=False,
    bind=engine
)

#CLASSSE de base pour tous les models sqlalchemy 
Base=declarative_base()