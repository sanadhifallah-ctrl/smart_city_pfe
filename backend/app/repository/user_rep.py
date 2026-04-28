from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate


def create_user(db:Session,Data:UserCreate):
    new_user=User(
        full_name=Data.full_name,
        email=Data.email,
        hashed_password=Hash_password(Data.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_by_id(db:Session,id_user:int):
    return db.query(User).filter(User.id==id_user).first()

def update_user_password(db:Session,user:User,hashed_password:str):
    user.password=hashed_passwordpassword
    db.commit()
    db.refresh(user)
    
    return user


def delete_use(db:Session,user:User,id_user:int):
    user=get_user_by_id(db,id_user)
    if user :
       db.delete(user) 
       db.commit()
    return user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_all_users(db: Session):
    return db.query(User).all()

def update_user(db: Session, user: User, data: UserUpdate):
    if data.full_name:
        user.full_name = data.full_name
    if data.email:
        user.email = data.email
    if data.phone_number:
        user.phone_number = data.phone_number
    db.commit()
    db.refresh(user)
    return user