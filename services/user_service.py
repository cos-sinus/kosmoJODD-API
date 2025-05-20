from repositories import UserRepository, UserCreateDto
from models import UserSchema
from pydantic import BaseModel, EmailStr
from typing import List
from jwt import encode
import os


class SigninDto(BaseModel):
    email: EmailStr
    password: str


class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def signup(self, user_data: UserCreateDto) -> UserSchema:
        return self.user_repo.create(user_data)
    
    def _generate_token(self, user_id: int, is_admin: bool) -> str:
            payload = {
                'user_id': str(user_id),
                'is_admin': str(int(is_admin)),
            }
            print("Шифрую в токен", payload)
            return encode(payload, os.getenv('JWT_SECRET'), algorithm='HS256')

    def signin(self, signin_data: SigninDto):
        user = self.user_repo.get_by_email(signin_data.email)
        if user.password == signin_data.password:
            token = self._generate_token(user.id, user.is_admin)
            return token
        raise Exception("Пароль неверный")

    def me(self, user_id: int):
        return self.user_repo.get_by_id(user_id)

    def get_all(self) -> List[UserSchema]:
        return self.user_repo.get_all()