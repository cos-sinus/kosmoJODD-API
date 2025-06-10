from repositories import RequestRepository, RequestCreateDto
from typing import List
from models import RequestSchema


class RequestService:
    def __init__(self, request_repository: RequestRepository):
        self.request_repository = request_repository

    def create(self, request: RequestCreateDto) -> None:
        self.request_repository.create(request)
    
    def get_all(self) -> List[RequestSchema]:
        return self.request_repository.get_all()
    
    def decline_request(self, request_id: int) -> None:
        self.request_repository.decline_request(request_id)