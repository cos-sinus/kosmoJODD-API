from repositories import UserRepository, UserCreateDto
from models import UserSchema

class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def signup(self, user_data: UserCreateDto) -> UserSchema:
        return self.user_repo.create(user_data)