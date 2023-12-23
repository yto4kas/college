from src.server.router import Router
from src.database.models import BaseModelModify
from .auth_resolver import login

class AuthRouter(Router):
    def __init__(self, name, model: type[BaseModelModify]):
        super(AuthRouter, self).__init__(name, model)
        self.router.add_api_route('/login', self.login, methods=["get"])

    def login(self, name: str, password: str):
        return login(name, password)
