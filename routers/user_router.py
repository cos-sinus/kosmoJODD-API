from controllers import UserController
from flask import Blueprint


class UserRouter:
    def __init__(self, controller: UserController):
        self.controller = controller
        self.router = Blueprint("user", __name__)
        self._setup_routes()

    def _setup_routes(self):
        self.router.add_url_rule("/signup/", view_func=self.controller.signup,methods=["POST"], endpoint="signup")