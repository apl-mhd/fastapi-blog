from operator import ge
from fastapi import APIRouter, status,HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends 
from typing import List
from .. import schemas, database, models, hashing

Hash = hashing.Hash


get_db = database.get_db

router = APIRouter()

@router.get('/blog', response_model=List[schemas.ShowBlog], tags=['blogs'])
def all(db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@router.post('/blog', status_code=status.HTTP_201_CREATED, tags=['blogs'])
def create(request: schemas.Blog, db:Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog



@router.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['blogs'])
def destroy(id, db:Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return 'done'

@router.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['blogs'])
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id) 
    #return blog.first()
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'blog with id {id} not found')
    blog.update({'title': request.title, 'body': request.body})
    db.commit()
    
    return 'updated'



@router.get('/blog/{id}', status_code=200, response_model=schemas.ShowBlog, tags=['blogs'])
def show(id, db:Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Blog with id {id} is not available")
    return blog


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