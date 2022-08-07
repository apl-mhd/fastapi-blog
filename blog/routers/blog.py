from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from schemas import ShowBlog
import schemas
from models import Blog


router =  APIRouter(
    prefix= '/blog',
    tags=['blogs']
)



@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = Blog(title= request.title, body= request.body, user_id = request.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.delete('/{id}')
def destroy(id, db:Session = Depends(get_db)):
    
    blog = db.query(Blog).filter(Blog.id == id) 
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"blog id {id} not found")
    
    blog.delete(synchronize_session=False)
    db.commit()
    return {'ok': True}

@router.put('/{id}', status_code = status.HTTP_202_ACCEPTED)
def update(id, request:schemas.Blog, db:Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id)
    
    if not blog.first():
        
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,  detail = f"Blog with id {id} is not avilable")
    
    blog.update({'title':request.title,  'body': request.body})
    db .commit()   
    return {'ok': True}



@router.get('/', response_model=List[ShowBlog])
def all(db:Session = Depends(get_db)):
    print('helllo-------------------------------')
    return db.query(Blog).all()

