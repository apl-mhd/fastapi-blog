from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models import User
from schemas import ShowBlog
import schemas
from hashing import Hash


router = APIRouter(
    prefix='/user'
)


@router.post('/', response_model=schemas.ShowUser, tags=['users'])
def create_user(request:schemas.User, db:Session = Depends(get_db)):
    new_user = User(name = request.name, email = request.email, password= Hash.hashed_password(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



@router.get('/', response_model=List[schemas.ShowUser], tags=['users'])
def user_all(db:Session = Depends(get_db)):
    users = db.query(User).all()
    return users

@router.get('/{id}', response_model=schemas.ShowUser, tags=['users'])
def get_user(id, db:Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} not found")
    return user

    