from sqlalchemy.orm.session import Session
from pydantic import BaseModel
from datetime import datetime
from models import RequestStatus, Request, RequestSchema

class RequestCreateDto(BaseModel):
    user_id: int
    camera_satellite_id: int
    target_satellite_id: int
    request_time: datetime | None = None


class RequestRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_status(self, title: str):
        request_status = RequestStatus(title=title)
        self.db.add(request_status)
        self.db.commit()

    def create(self, request: RequestCreateDto):
        request = Request(**request.model_dump(), status_id=1)
        self.db.add(request)
        self.db.commit()

    def get_all(self):
        return [RequestSchema.model_validate(request, from_attributes=True) for request in self.db.query(Request).all()]
    
    def decline_request(self, request_id: int):
        request = self.db.query(Request).filter(Request.id == request_id).first()
        request.status_id = 2
        self.db.commit()