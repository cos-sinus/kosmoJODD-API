from sqlalchemy.orm.session import Session
from pydantic import BaseModel, EmailStr
from models import User, UserSchema


class UserCreateDto(BaseModel):
    email: EmailStr
    name: str
    is_admin: bool = False
    password: str


class UserRepository:
    """# Класс для работы с таблицей пользователей"""
    def __init__(self, db: Session):
        self.db = db

    def create(self, user_data: UserCreateDto) -> UserSchema:
        user = User(**user_data.model_dump()) # Переводим данные из dto в модель
        self.db.add(user) # Добавляем пользователя в базу
        self.db.commit() # Сохраняем
        self.db.refresh(user) # Обновляем данные пользователя (id, ...)
        return UserSchema.model_validate(user, from_attributes=True) # Переводим в схему и возвращаем
    

