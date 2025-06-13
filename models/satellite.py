from pydantic import BaseModel, EmailStr
from models.base import Base
from sqlalchemy import Column, Float, Integer, String, Boolean, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime


# получается нада добавить в базу поле с наличием камеры и фокусным расстоянием
class SatelliteSchema(BaseModel):
    id: int|None = None
    name: str
    full_TLE: str
    camera: bool = False

    cutalog_num: str # Номер спутника в базе данных NORAD
    classfic: str # Классификация (U=Unclassified — не секретный)
    international_des_year: int # Международное обозначение (последние две цифры года запуска)
    international_des_num: int # Международное обозначение (номер запуска в этом году)
    international_des_push: str # Международное обозначение (часть запуска)
    epoch_year: int # 	Год эпохи (последние две цифры)
    epoch_day: float # Время эпохи (целая часть — номер дня в году, дробная — часть дня)
    first_meanmotion_a: float # Первая производная от среднего движения (ускорение), делённая на два [виток/день^2]
    second_meanmotion_a: str # Вторая производная от среднего движения, делённая на шесть
    drag_term_b: str # Коэффициент торможения B*
    nul: int # Изначально — типы эфемерид, сейчас — всегда число 0
    el_set_num: int # Номер (версия) элемента

    inclin_digrees: float # Наклонение в градусах
    ascension: float # Долгота восходящего узла в градусах
    eccentricity: float # Эксцентриситет (подразумевается, что число начинается с десятичного разделителя)
    perigee_arg: float # Аргумент перицентра в градусах
    meananomaly: float # Средняя аномалия в градусах
    meanmotion: float # Частота обращения (оборотов в день) (среднее движение) [виток/день]
    revolution_num: int # Номер витка на момент эпохи

    checksum: int # Контрольная сумма по модулю 10


class SatelliteCrossSchema(BaseModel):
    id: int
    target_id: int
    name: str
    time_visible: datetime


class Satellite(Base):
    __tablename__ = "satellites"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True)
    full_TLE = Column(Text, unique=True)
    camera = Column(Boolean, default=False)######################################################

    cutalog_num = Column(String(255)) # Номер спутника в базе данных NORAD
    classfic = Column(String(255)) # Классификация (U=Unclassified — не секретный)
    international_des_year = Column(Integer) # Международное обозначение (последние две цифры года запуска)
    international_des_num = Column(Integer) # Международное обозначение (номер запуска в этом году)
    international_des_push = Column(String(255)) # Международное обозначение (часть запуска)
    epoch_year = Column(Integer) # 	Год эпохи (последние две цифры)
    epoch_day = Column(Float) # Время эпохи (целая часть — номер дня в году, дробная — часть дня)
    first_meanmotion_a = Column(Float) # Первая производная от среднего движения (ускорение), делённая на два [виток/день^2]
    second_meanmotion_a = Column(String(255)) # Вторая производная от среднего движения, делённая на шесть
    drag_term_b = Column(String(255)) # Коэффициент торможения B*
    nul = Column(Integer) # Изначально — типы эфемерид, сейчас — всегда число 0
    el_set_num = Column(Integer) # Номер (версия) элемента

    inclin_digrees = Column(Float) # Наклонение в градусах
    ascension = Column(Float) # Долгота восходящего узла в градусах (подразумевается, что число начинается с десятичного разделителя)
    eccentricity = Column(Float) # Эксцентриситет (подразумевается, что число начинается с десятичного разделителя)
    perigee_arg = Column(Float) # Аргумент перицентра в градусах
    meananomaly = Column(Float) # Средняя аномалия в градусах
    meanmotion = Column(Float) # Частота обращения (оборотов в день) (среднее движение) [виток/день]
    revolution_num = Column(Integer) # Номер витка на момент эпохи

    checksum = Column(Integer) # Контрольная сумма по модулю 10

    camera_requests = relationship(
        "Request",
        back_populates="camera_satellite",
        foreign_keys="[Request.camera_satellite_id]",
    )

    target_requests = relationship(
        "Request",
        back_populates="target_satellite",
        foreign_keys="[Request.target_satellite_id]",
    )