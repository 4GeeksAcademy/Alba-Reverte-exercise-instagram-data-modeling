import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    user_name = Column(String(50), nullable=False)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    comment = relationship ('comment', backref="user")
    post = relationship ('post', backref="user")

class Post(Base):
    __tablename__ = 'post'
    
    id = Column(Integer, primary_key=True)
    date = Column(Integer)
    description = Column(String(250))
    user_id = Column(Integer, ForeignKey ("user.id"))
    media_id = Column(Integer, ForeignKey ("media.id"))
    comment = relationship ('comment', backref="post")

class Comment(Base):
    __tablename__ = 'comment'
    
    id = Column(Integer, primary_key=True)
    created_at = Column(Integer)
    comment = Column(String(250))
    user_id = Column(Integer, ForeignKey ("user.id"))
    post_id = Column(Integer, ForeignKey ("post.id"))

class Media(Base):
    __tablename__ = 'media'
    
    id = Column(Integer, primary_key=True)
    url = Column(String(250))
    type = Column(enumerate(MediaType))
    post = relationship ('post', backref="media")
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
