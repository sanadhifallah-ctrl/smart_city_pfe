from datetime import datetime,timedelta,timezone
from passlib.context import CryptContext
from app.core.config import settings
from jose import jwt

pwd_context=CryptContext(
    schemes=["bcrypt"]
)

#register
def Hash_password(password:str)->str :
    return pwd_context.hash(password)

#login
def verify_password(plain_password:str, hashed_password:str)->bool:
    return pwd_context.verify(plain_password,hashed_password)


#creation de token(user) -> login 
def create_accesss_token(data:dict):
    #on prend info user 
    to_encodde=data.copy()
    
    #cal date d expiration 
    expire=datetime.now(timezone.utc)+timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    #add exipre dans  to_encodde 
    to_encodde.update({"exp":expire})
    
    #generer token 
    encode_jwt=jwt.encode(
        to_encodde,
        settings.SECRET_KEY,
        settings.ALGORITHM
    )
    return encode_jwt
