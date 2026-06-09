# pyrefly: ignore [missing-import]
from sqlalchemy import Column, Integer, String
from app.core.database import Base
 
class User(Base):
    __table__="users"

    id= Column(Integer, primary_key=True, index=True)
    name=Column(String, unique=True, index=True)
    email=Column(String, unique=True, index=True)
    password=Column(String, nullable=False)
    role=Column(String, nullable=False, default="user")
    
