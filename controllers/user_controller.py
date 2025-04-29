from services import UserService, SigninDto
from flask import request, jsonify
from repositories import UserCreateDto


class UserController:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def signup(self):
        body = request.get_json()
        user_data = UserCreateDto(**body)
        user = self.user_service.signup(user_data)
        return jsonify(user.model_dump()), 201
    
    def signin(self):
        try:
            body = request.get_json()
            signin_data = SigninDto(**body)
            token = self.user_service.signin(signin_data)
            return jsonify({"token" : token}), 200
        except Exception as e:
            return jsonify({"error" : str(e)}), 400