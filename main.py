from flask import Flask
from models import get_db, Base, engine
from repositories import UserRepository, SatelliteRepository
from services import UserService, SatelliteService
from controllers import UserController, SatelliteController
from core import GeometryEngine
from routers import UserRouter, SatelliteRouter
from dotenv import load_dotenv
from flask_cors import CORS


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    load_dotenv(override=True)
    with get_db() as db:
        g_e = GeometryEngine()

        user_repo = UserRepository(db)
        satellite_repo = SatelliteRepository(db)
        user_service = UserService(user_repo)
        satellite_service = SatelliteService(satellite_repo, g_e)
        user_controller = UserController(user_service)
        satellite_controller = SatelliteController(satellite_service)
        user_router = UserRouter(user_controller)
        satellite_router = SatelliteRouter(satellite_controller)
        app = Flask(__name__)
        CORS(app)
        app.register_blueprint(user_router.router, url_prefix="/users")
        app.register_blueprint(satellite_router.router, url_prefix="/satellites")
        app.run(host="0.0.0.0", port=5000)
