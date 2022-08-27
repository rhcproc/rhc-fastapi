
from fastapi import FastAPI, Depends

# Routers
from handlers.api.auth import auth
from handlers.api.v1 import api as api_v1

#views
from views.index import api as index_api

 

def get_app_for_applied_routes(app: FastAPI):
    # Register Routers
    app.include_router(auth, prefix="/api/auth")
    app.include_router(api_v1, prefix='/api/v1')

    app.include_router(index_api)


   

    return app