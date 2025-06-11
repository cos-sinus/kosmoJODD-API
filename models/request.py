from models.base import Base
from sqlalchemy import Column, Integer, DateTime, ForeignKey, String
from pydantic import BaseModel
from datetime import datetime


class RequestStatus(Base):
    __tablename__ = 'request_status'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))

class Request(Base):
    __tablename__ = "requests"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    camera_satellite_id = Column(Integer, ForeignKey("satellites.id"))
    target_satellite_id = Column(Integer, ForeignKey("satellites.id"))
    request_time = Column(DateTime)
    created = Column(DateTime, default=datetime.now)
    status_id = Column(Integer, ForeignKey("request_status.id"))
    comment = Column(String(255), nullable=True)
    file_path = Column(String(255), nullable=True)


class RequestStatusSchema(BaseModel):
    id: int
    title: str

class RequestSchema(BaseModel):
    id: int
    user_id: int # кто формирует запрос
    camera_satellite_id: int #спутник который фотографирует
    target_satellite_id: int #спутник который фотографируют
    request_time: datetime #время проведеня съемки
    created: datetime #время создания запроса
    status_id: int #статус запроса
    comment: str | None = None #комментарий к запросу
    file_path: str | None = None