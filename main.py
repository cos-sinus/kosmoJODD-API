from flask import Flask
from models import get_db, Base, engine
from repositories import UserRepository, SatelliteRepository, RequestRepository
from services import UserService, SatelliteService, RequestService
from controllers import UserController, SatelliteController, RequestController
from core import GeometryEngine
from routers import UserRouter, SatelliteRouter, RequestRouter
from dotenv import load_dotenv
from flask_cors import CORS


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    load_dotenv(override=True)
    with get_db() as db:
        g_e = GeometryEngine()

        user_repo = UserRepository(db)
        satellite_repo = SatelliteRepository(db)
        request_repo = RequestRepository(db)

        user_service = UserService(user_repo)
        satellite_service = SatelliteService(satellite_repo, g_e)
        request_service = RequestService(request_repo)

        user_controller = UserController(user_service)
        satellite_controller = SatelliteController(satellite_service)
        request_controller = RequestController(request_service)

        user_router = UserRouter(user_controller)
        satellite_router = SatelliteRouter(satellite_controller)
        request_router = RequestRouter(request_controller)

        app = Flask(__name__)
        CORS(app)
        app.register_blueprint(user_router.router, url_prefix="/users")
        app.register_blueprint(satellite_router.router, url_prefix="/satellites")
        app.register_blueprint(request_router.router, url_prefix="/requests")
        app.run(host="0.0.0.0", port=5000)
