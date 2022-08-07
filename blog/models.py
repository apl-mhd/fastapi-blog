from operator import index
from sqlalchemy import Integer, String, Column, ForeignKey
from database import Base
from sqlalchemy.orm import relationship
from typing import List

class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    creator = relationship('User', back_populates='blogs')
    

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    
    blogs = relationship('Blog', back_populates='creator')
    
    
    
    
    
    
    

