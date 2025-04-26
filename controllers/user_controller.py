from services import UserService
from flask import request, jsonify
from repositories import UserCreateDto


class UserController:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def signup(self):
        body = request.get_json()
        user_data = UserCreateDto(**body)
        user = self.user_service.signup(user_data)
        return 201, jsonify(user.model_dump())