from controllers import RequestController
from flask import Blueprint


class RequestRouter:
    def __init__(self, controller: RequestController):
        self.controller = controller
        self.router = Blueprint("request", __name__)
        self._setup_routes()

    def _setup_routes(self):
        self.router.add_url_rule("/", view_func=self.controller.create_request, methods=["POST"], endpoint="create_request")
        self.router.add_url_rule("/", view_func=self.controller.get_all_requests, methods=["GET"], endpoint="get_all_requests")
        self.router.add_url_rule("/decline/<int:request_id>", view_func=self.controller.decline_request, methods=["PUT"], endpoint="decline_request")
        self.router.add_url_rule("/accept/<int:request_id>", view_func=self.controller.accept_request, methods=["PUT"], endpoint="accept_request")
