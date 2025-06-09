from services import RequestService
from repositories import RequestCreateDto
from utils.decorators import authorized
from flask import request, jsonify



class RequestController:
    def __init__(self, request_service: RequestService):
        self.request_service = request_service

    @authorized
    def create_request(self, user_id: int):
        data = request.get_json()
        request_data = RequestCreateDto(**data, user_id=user_id)
        self.request_service.create(request_data)
        return jsonify({"message" : "Запрос успешно создан"}), 201
