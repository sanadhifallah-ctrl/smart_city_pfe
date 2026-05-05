#import 
from app.schema.user import UserCreate
from app.repository.user_rep import create_user,get_user_by_email
from sqlalchemy.orm import Session
from app.core.securite import Hash_password , verify_password
from fastapi import HTTPException, status
import re
from passlib.context import CryptContext
from app.schema.user import UserUpdate
from app.repository.user_rep import get_user_by_id, update_user
from app.schema.user import UpdatePassword


#helpers 
def _email_used(db: Session, email: str, id_user: int | None):

    existing_user = get_user_by_email(db, email)

    if existing_user and (id_user is None or existing_user.id != id_user):

        raise HTTPException(

            status_code=status.HTTP_409_CONFLICT,

            detail="email already exists"

        )
    

def _validate_pass(password: str):
    if len(password) < 8:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="password must contain 8 characters"
        )

    if not re.search(r"[A-Z]", password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="password must contain uppercase"
        )

    if not re.search(r"[a-z]", password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="password must contain lowercase"
        )

    if not re.search(r"[0-9]", password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="password must contain numbers"
        )
    



def register_user(user_data: UserCreate, db: Session):

    _email_used(db, user_data.email, None)

    _validate_pass(user_data.password)

    hashed_pw = Hash_password(user_data.password)

    new_user = create_user(

        db,

        user_data.full_name,

        user_data.email,

        hashed_pw

    )

    

    return new_user

  
def login_user(db: Session, email, password):

    user = get_user_by_email(db, email)

    if not user:

        raise HTTPException(

            status_code=status.HTTP_404_NOT_FOUND,

            detail="user not found"

        )

    if not verify_password(password, user.password):

        raise HTTPException(

            status_code=status.HTTP_401_UNAUTHORIZED,

            detail="incorrect password"

        )

    return user

def update_profile(db: Session, user_id: int, user_data: UserUpdate):

    user = get_user_by_id(db, user_id)

    if not user:

        raise HTTPException(

            status_code=status.HTTP_404_NOT_FOUND,

            detail="user not found"

        )

    if user_data.email:

        _email_used(db, user_data.email, user_id)

    modified_user = update_user(

        db, user_id, full_name=user_data.full_name, email=user_data.email

    )

    return modified_user

def update_password(user_id: int, db: Session, data: UpdatePassword):

    user = get_user_by_id(db, user_id)

    if not user:

        raise HTTPException(

            status_code=status.HTTP_404_NOT_FOUND,

            detail="user not found"

        )

    if not verify_password(data.old_password, user.password):

        raise HTTPException(

            status_code=status.HTTP_401_UNAUTHORIZED,

            detail="Current password is incorrect"

        )

    if data.old_password == data.new_password:

        raise HTTPException(

            status_code=status.HTTP_400_BAD_REQUEST,

            detail="New password must be different from current password"

        )

    _validate_pass(data.new_password)

    hashed_pw = Hash_password(data.new_password)

    update_user(db, user_id, password=hashed_pw)

    return {"message": "Password updated successfully"}

def forgot_password_service():
    # TODO: implement forgot password logic
    pass