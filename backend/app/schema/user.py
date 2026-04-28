from pydantic import BaseModel,EmailStr,ConfigDict
from datetime import datetime
from app.models.user import UserRole
from typing import Optional

class UserCreate(BaseModel):
    full_name:str
    email:EmailStr
    password:str

class UserUpdate(BaseModel):
    full_name:Optional[str]=None
    email:Optional[EmailStr]=None

class UpdatePassword(BaseModel):
    current_password:str
    new_password:str  

class UserResponse(BaseModel):
    id:int
    full_name:int
    email:EmailStr
    role:UserRole
    is_active:bool 
    created_at: datetime

    model_config=ConfigDict (from_attributes=True)
