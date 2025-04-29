from flask import Flask, jsonify
from core.tle_encoder import TLE_encoder
from models import get_db, Base, engine
from repositories import UserRepository
from services import UserService
from controllers import UserController
from routers import UserRouter
from dotenv import load_dotenv


# @app.route("/")
# def index():
#     tles = TLE_encoder.open_TLEfile("TLE/TLE_msu.txt")
#     tles += TLE_encoder.open_TLEfile("TLE/TLE_astroportal.txt")
#     return jsonify([tle.model_dump() for tle in tles]) # генератор


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    load_dotenv(override=True)
    with get_db() as db:
        user_repo = UserRepository(db)
        user_service = UserService(user_repo)
        user_controller = UserController(user_service)
        user_router = UserRouter(user_controller)
        app = Flask(__name__)
        app.register_blueprint(user_router.router, url_prefix="/users")
        app.run(host="0.0.0.0", port=5000)