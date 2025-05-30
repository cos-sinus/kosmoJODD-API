from sqlalchemy.orm.session import Session
from pydantic import BaseModel, EmailStr
from models import Satellite, SatelliteSchema
from typing import List
from sqlalchemy.exc import IntegrityError


class SatelliteRepository:
    """# Класс для работы с таблицей спутников"""
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: SatelliteSchema):
        try:
            satel = Satellite(**data.model_dump()) # Переводим данные из dto в модель
            self.db.add(satel) # Добавляем пользователя в базу
            self.db.commit() # Сохраняем
            self.db.refresh(satel) # Обновляем данные пользователя (id, ...)
            return SatelliteSchema.model_validate(satel, from_attributes=True) # Переводим в схему и возвращаем
        except IntegrityError:
            print("Спутник был")
            self.db.rollback()
            return
        
    def get_all(self) -> List[SatelliteSchema]:
        return [
            SatelliteSchema.model_validate(satel, from_attributes=True)
            for satel in self.db.query(Satellite).all()
        ]