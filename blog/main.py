from ast import Not
import email
from hashlib import new
from tkinter.messagebox import NO
from urllib import response
from fastapi import FastAPI, Depends, status, Response, HTTPException
import schemas, models
from database import engine,session_local
from sqlalchemy.orm import Session
from models import Blog, User
from schemas import ShowBlog
from routers import blog, user, authentication

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)

