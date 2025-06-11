from repositories import RequestRepository, RequestCreateDto
from utils.request_file_storage import RequestFileStorage
from werkzeug.datastructures import FileStorage
from typing import List
from models import RequestSchema


class RequestService:
    def __init__(
            self, 
            request_repository: RequestRepository,
            request_file_storage: RequestFileStorage
        ):
        self.request_repository = request_repository
        self.request_file_storage = request_file_storage

    def create(self, request: RequestCreateDto) -> None:
        self.request_repository.create(request)
    
    def get_all(self) -> List[RequestSchema]:
        return self.request_repository.get_all()
    
    def get_unchecked_requests(self) -> List[RequestSchema]:
        return self.request_repository.get_unchecked_requests()
    
    def decline_request(self, request_id: int, comment: str) -> None:
        self.request_repository.decline_request(request_id, comment)

    def accept_request(self, request_id: int, file: FileStorage) -> None:
        file_path = self.request_file_storage.upload_file(file)
        self.request_repository.accept_request(request_id, file_path)

    def get_by_user_id(self, user_id: int) -> List[RequestSchema]:
        return self.request_repository.get_by_user_id(user_id)