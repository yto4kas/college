from src.server.resolver import Resolver
from fastapi import APIRouter
from src.database.models import BaseModelModify

class Router:

    def __init__(self, name, model: type[BaseModelModify]):
        self.name = name
        self.model = model
        self.resolver = Resolver(model)

        self.router = APIRouter(prefix=f'/{name}', tags=[name])
        self.addEndpoints()

    def addEndpoints(self):
        m = self.model

        @self.router.get("/id")
        def get(object_id: int):
            return self.resolver.get(object_id)

        @self.router.post("/create")
        def create(model: m):
            self.resolver.create(model)

        @self.router.delete("/delete")
        def delete(object_id: int):
            return self.resolver.remove(object_id)

        @self.router.put("/update")
        def update(object_id: int, new_data: m):
            return self.resolver.update(object_id=object_id, new_data=new_data)

        @self.router.get("/")
        def get_all():
            return self.resolver.get_all()
