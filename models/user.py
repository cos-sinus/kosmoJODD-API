from pydantic import BaseModel, EmailStr
from models.base import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime

#Схема для 3 бд + модели для них


class UserSchema(BaseModel): # Схема
    id: int
    email: EmailStr
    name: str
    is_admin: bool
    password: str
    created: datetime


class User(Base): # Модель
    """# Привязка к базе данных"""
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), unique=True)
    name = Column(String(255))
    is_admin = Column(Boolean, default=False)
    password = Column(String(255))
    created = Column(DateTime, default=datetime.now)
