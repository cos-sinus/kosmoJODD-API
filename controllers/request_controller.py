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
        request_time = datetime.strptime(data["request_time"], "%d-%m-%Y %H:%M:%S")
        data["request_time"] = request_time
        request_data = RequestCreateDto(**data, user_id=user_id)
        self.request_service.create(request_data)
        return jsonify({"message" : "Запрос успешно создан"}), 201
    
    @is_admin
    def get_all_requests(self, user_id: int):
        return jsonify([request.model_dump() for request in self.request_service.get_all()]), 200

    @is_admin
    def decline_request(self, user_id: int, request_id: int):
        self.request_service.decline_request(request_id)
        return jsonify({"message" : "Запрос успешно отклонен"}), 200