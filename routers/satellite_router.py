from controllers import SatelliteController
from flask import Blueprint


class SatelliteRouter:
    def __init__(self, controller: SatelliteController):
        self.controller = controller
        self.router = Blueprint("satellite", __name__)
        self._setup_routes()

    def _setup_routes(self):
        self.router.add_url_rule("/", view_func=self.controller.get_all, methods=["GET"], endpoint="get_all_satellites")