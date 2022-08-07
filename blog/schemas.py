import email
from pydantic import BaseModel
from typing import Optional, List


class Blog(BaseModel):
    title: str
    body: str
    user_id: int
    published: Optional[bool]
    class Config():
        orm_mode = True
    
class User(BaseModel):
    id: int
    name: str
    email: str
    password: str
    class Config():
        orm_mode = True  
        
class ShowUser(BaseModel):
    id: int
    name: str
    email: str
    password: str
    blogs : List[Blog] = []
    class Config():
        orm_mode = True  

class ShowBlog(Blog):
    id: int
    creator: User
    class Config():
        orm_mode = True
        

        

