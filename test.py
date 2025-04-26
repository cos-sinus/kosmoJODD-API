from models import get_db
from repositories import UserRepository, UserCreateDto


if __name__ == "__main__":
    with get_db() as db:
        repo = UserRepository(db)
        user_data = UserCreateDto(
            email="test@test.ru",
            name="test",
            password="test"
        )
        repo.create(user_data)