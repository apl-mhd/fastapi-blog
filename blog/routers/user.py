from operator import ge
from fastapi import APIRouter, status,HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends 
from typing import List
from .. import schemas, database, models, hashing

Hash = hashing.Hash
get_db = database.get_db

router = APIRouter()


@router.post('/user', response_model=schemas.ShowUser, tags=['users'])
def  create_user(request: schemas.User, db: Session = Depends(get_db)):
    
    new_user = models.User( name = request.name, email = request.email,
                           password = Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user


@router.get('/user/{id}', response_model=schemas.ShowUser, tags=['users'])
def get_user(id:int, db:Session = Depends(get_db)):
    
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail= f"Blog with id {id} is not available")
    return user