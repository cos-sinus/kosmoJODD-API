from sqlalchemy.orm.session import Session
from pydantic import BaseModel
from datetime import datetime
from models import RequestStatus

class RequestCreateDto(BaseModel):
    user_id: int
    camera_satellite_id: int
    target_satellite_id: int
    request_time: datetime


class RequestRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_status(self, title: str):
        request_status = RequestStatus(title=title)
        self.db.add(request_status)
        self.db.commit()

    def create(self, request: RequestCreateDto):
        pass