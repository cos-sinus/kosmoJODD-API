from models import Base, get_db, engine
from repositories import RequestRepository

STATUSES = [
    "В процессе",
    "Отклонено",
    "Завершено"
]

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    with get_db() as db:
        repo = RequestRepository(db)
        for status in STATUSES:
            repo.create_status(status)
