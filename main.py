from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app = FastAPI()



@app.get('/blog/unpublished')
def unpublished():
    return {'data': True}

@app.get('/blog/{id}')
def show(id:int):
    return {'data': id}

@app.get('/blog/')
def index(limit, a: Optional[str] = None):
    return f'no of blog {limit}'

@app.get('/about/{id}')
def about(id):
    return {'data': id}

@app.get('/blog/{id}/comments')
def comment(id):
    return {'data': {1,2,3}}



class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(request: Blog):
    return request
    #return {'data': 'blog is created'}
    
    
