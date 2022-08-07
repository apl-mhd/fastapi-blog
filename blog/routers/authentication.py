from lib2to3.pgen2 import token
import secrets
from fastapi import APIRouter, Depends, HTTPException, status
import schemas
from database import session_local, get_db
from sqlalchemy.orm import Session
from models import User
from hashing import Hash
from jose import jwt
from tokn import create_access_token
router = APIRouter()


@router.post('/login')
def login(request: schemas.Login, db:Session = Depends(get_db)):
    
    user = db.query(User).filter(User.email == request.email).first()
    
    if not user:
        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail=f' user {request.email} not found')
    
    if not  Hash.verify_password(request.password, user.password):
        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail=f' password  not matched')
    access_token = create_access_token(data={"sub": user.email})

    return access_token
    #return user
    