import uvicorn
import fastapi
from fastapi.responses import RedirectResponse
from src.server.routers_holder import routers
from src.database.db_manager import db

app = fastapi.FastAPI()

[app.include_router(router) for router in routers]

@app.router.get('/', include_in_schema=False)
def index() -> RedirectResponse:
    return RedirectResponse('/docs')


if __name__ == '__main__':
    db.checkDatabase('src/database/base.sql')

    uvicorn.run("server:app", reload=False, host='127.0.0.1')

