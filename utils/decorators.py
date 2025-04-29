from typing import Callable
from flask import request, jsonify
from jwt import decode, DecodeError
from jwt.exceptions import InvalidSignatureError
import os


def authorized(f: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        headers = request.headers
        bearer_token = headers.get("Authorization")
        print("Bearer token: ", bearer_token)
        if not bearer_token:
            return jsonify({"message": "Unauthorized"}), 401
        try:
            token = bearer_token.split()[1]
            user_id = int(decode(token, os.getenv("JWT_SECRET"), algorithms=["HS256"]).get("user_id"))
            print("Авторизирован пользователь: ", user_id)
            return f(*args, **kwargs, user_id=user_id)
        except InvalidSignatureError as e:
            return jsonify({"message": "Invalid token"}), 419
        except DecodeError as e:
            print('Ошибка расшифровки токена', e)
            return jsonify({"message": "Ошибка расшифровки токена - Not enough segments"}), 419

    return wrapper

def is_admin(f: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        headers = request.headers
        bearer_token = headers.get("Authorization")
        if not bearer_token:
            return jsonify({"message": "Unauthorized"}), 401
        try:
            token = bearer_token.split()[1]
            data = decode(token, os.getenv("JWT_SECRET"), algorithms=["HS256"])
            is_admin = bool(int(data.get("is_admin")))
            user_id = int(data.get("user_id"))
            print("Авторизирован пользователь: ", user_id)
            if not is_admin:
                return jsonify({"message": "Permission denied"}), 403
            return f(*args, **kwargs, user_id=user_id)
        except InvalidSignatureError as e:
            return jsonify({"message": "Invalid token"}), 419
        except DecodeError as e:
            print('Ошибка расшифровки токена', e)
            return jsonify({"message": "Ошибка расшифровки токена - Not enough segments"}), 419

    return wrapper