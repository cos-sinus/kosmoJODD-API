from sqlalchemy.orm.session import Session
from pydantic import BaseModel, EmailStr
from models import User, UserSchema


class UserCreateDto(BaseModel):
    email: EmailStr
    name: str
    is_admin: bool = False
    password: str

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user_data: UserCreateDto) -> UserSchema:
        user = User(**user_data.model_dump())
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return UserSchema.model_validate(user, from_attributes=True)
    

