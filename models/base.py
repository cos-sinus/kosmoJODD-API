from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import OperationalError
from sqlalchemy import create_engine
from contextlib import contextmanager
from dotenv import load_dotenv
import os, time


Base = declarative_base()
load_dotenv(override=True)


# Подключение к базе данных SQLite
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    DATABASE_URL,
    echo=True, # логирование
    pool_pre_ping=True,
    pool_recycle=3600,
    max_overflow=20,
    pool_size=10
)
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=True, bind=engine))


@contextmanager
def get_db():
    session = None
    for attempt in range(5):  # Пробуем 5 раз
        try:
            session = SessionLocal()
            yield session
            return  # Если успех — выходим
        except OperationalError:
            print(f"[{attempt + 1}/5] База недоступна, пробую снова...")
            time.sleep(5)
        finally:
            if session:
                session.close()  # Закрываем сессию всегда
    raise Exception("Не удалось подключиться к базе после 5 попыток")

if __name__ == "__main__":
    with get_db() as db:
        print(db)