from sqlalchemy.orm.session import Session
from sqlalchemy.orm import joinedload
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
    
    def decline_request(self, request_id: int, comment: str):
        request = self.db.query(Request).filter(Request.id == request_id).first()
        request.status_id = 2
        request.comment = comment
        self.db.commit()

    def accept_request(self, request_id: int, file_path: str):
        request = self.db.query(Request).filter(Request.id == request_id).first()
        request.status_id = 3
        request.file_path = file_path
        self.db.commit()

    def get_by_user_id(self, user_id: int):
        return [
            RequestSchema.model_validate(request, from_attributes=True) 
            for request in self.db.query(Request).filter(Request.user_id == user_id).all()
        ]
    
    def get_unchecked_requests(self):
        return [
            RequestSchema.model_validate(request, from_attributes=True) 
            for request in self.db.query(Request)
            .options(
                joinedload(Request.status),
                joinedload(Request.camera_satellite),
                joinedload(Request.target_satellite)
            ).filter(Request.status_id == 1).all()
        ]