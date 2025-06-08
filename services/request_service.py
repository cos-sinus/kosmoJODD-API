from repositories import RequestRepository, RequestCreateDto


class RequestService:
    def __init__(self, request_repository: RequestRepository):
        self.request_repository = request_repository

    def create(self, request: RequestCreateDto) -> None:
        self.request_repository.create(request)
    
    
