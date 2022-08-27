from fastapi import FastAPI, Depends
from fastapi.responses import ORJSONResponse
from settings import Settings, __VERSION__
from handlers.depends.context import parse_request_body
from handlers import api

# # Routers
# from handlers.api.auth import auth
# from handlers.api.v1 import api as api_v1

# #views
# from views.index import api as index_api

# Middleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from starlette_context.middleware import RawContextMiddleware
# from app.middleware import HelloMiddleware


def create_app(settings: Settings) -> FastAPI:
    """Application Factory"""
    app = FastAPI(
        title=settings.app_name,
        description=settings.description,
        version=__VERSION__,
        terms_of_service=settings.term_of_service,
        contact={
            "name": settings.contact_name,
            "url": settings.contact_url,
            "email": settings.contact_email
        },
        docs_url=settings.docs_url,
        default_response_class=ORJSONResponse,
        dependencies=[
            Depends(parse_request_body),
        ],
    )

    # Built-in init
    settings.init_app(app)
    api.init_app(app, settings)

    # Extension/Middleware init
    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"])
    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=["*"])
    app.add_middleware(
        GZipMiddleware,
        minimum_size=1024)
    app.add_middleware(RawContextMiddleware)
    """
    # If you want to use middleware, you can add it here.
    app.add_middleware(HelloMiddleware)
    """

   
    
    # # Register Routers
    # app.include_router(auth, prefix="/api/auth")
    # app.include_router(index_api)
    # app.include_router(api_v1, prefix='/api/v1')

    return app