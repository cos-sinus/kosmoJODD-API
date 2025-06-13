from services import RequestService
from repositories import RequestCreateDto
from utils.decorators import authorized, is_admin
from flask import request, jsonify
from datetime import datetime



class RequestController:
    def __init__(self, request_service: RequestService):
        self.request_service = request_service

    @authorized
    def create_request(self, user_id: int):
        data = request.get_json()
        request_time = datetime.strptime(data["request_time"], "%d.%m.%Y, %H:%M:%S")
        data["request_time"] = request_time
        request_data = RequestCreateDto(**data, user_id=user_id)
        self.request_service.create(request_data)
        return jsonify({"message" : "Запрос успешно создан"}), 201
    
    @is_admin
    def get_all_requests(self, user_id: int):
        return jsonify([request.model_dump() for request in self.request_service.get_all()]), 200

    @is_admin
    def decline_request(self, user_id: int, request_id: int):
        data = request.get_json()
        comment = data.get("comment", None)
        self.request_service.decline_request(request_id, comment)
        return jsonify({"message" : "Запрос успешно отклонен"}), 200
    
    @is_admin
    def accept_request(self, user_id: int, request_id: int):
        file = request.files.get("file")
        if not file:
            return jsonify({"error": "Файл не найден"}), 400
        self.request_service.accept_request(request_id, file)
        return jsonify({"message" : "Запрос успешно одобрен"}), 200
    
    @authorized
    def get_requests_by_user_id(self, user_id: int):
        return jsonify([request.model_dump() for request in self.request_service.get_by_user_id(user_id)]), 200
    
    @is_admin
    def get_unchecked_requests(self, user_id: int):
        return jsonify([request.model_dump() for request in self.request_service.get_unchecked_requests()]), 200