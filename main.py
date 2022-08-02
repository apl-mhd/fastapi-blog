
from hashlib import new
from typing import List
from fastapi import Depends, FastAPI, status, Response, HTTPException
from  blog.database import engine, get_db
from sqlalchemy.orm import Session
from  blog import models, schemas
from passlib.context import CryptContext
from blog.hashing import Hash
from blog.routers import blog, user

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.post('/blog', status_code=status.HTTP_201_CREATED, tags=['blogs'])
# def create(request: schemas.Blog, db:Session = Depends(get_db)):
#     new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog

# @app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['blogs'])
# def destroy(id, db:Session = Depends(get_db)):
#     db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
#     db.commit()
#     return 'done'

# @app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['blogs'])
# def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id) 
#     #return blog.first()
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
#                             detail=f'blog with id {id} not found')
#     blog.update({'title': request.title, 'body': request.body})
#     db.commit()
    
#     return 'updated'
    
    

# @app.get('/blog', response_model=List[schemas.ShowBlog], tags=['blogs'])
# def all(db:Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs

# @app.get('/blog/{id}', status_code=200, response_model=schemas.ShowBlog, tags=['blogs'])
# def show(id, db:Session=Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Blog with id {id} is not available")
#         #response.status_code = status.HTTP_404_NOT_FOUND
#         #return {'detail': f"Blog with id {id} is not available"}
#     return blog


# @app.post('/user', response_model=schemas.ShowUser, tags=['users'])
# def  create_user(request: schemas.User, db: Session = Depends(get_db)):
    
#     new_user = models.User( name = request.name, email = request.email,
#                            password = Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
    
#     return new_user


# @app.get('/user/{id}', response_model=schemas.ShowUser, tags=['users'])
# def get_user(id:int, db:Session = Depends(get_db)):
    
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
#                             detail= f"Blog with id {id} is not available")
#     return user