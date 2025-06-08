from services import RequestService
from repositories import RequestCreateDto
from flask import request, jsonify



class RequestController:
    def __init__(self, request_service: RequestService):
        self.request_service = request_service

    def create_request(self):
        data = request.get_json()
        request_data = RequestCreateDto(**data)
        self.request_service.create(request_data)
        return jsonify({"message" : "Запрос успешно создан"}), 201
