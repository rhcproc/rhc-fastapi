"""
Application Management Module
"""
from fastapi import FastAPI
from handlers import create_app
from settings import settings
from mangum import Mangum
from fastapi.openapi.utils import get_openapi
from urls import get_app_for_applied_routes
from fastapi.staticfiles import StaticFiles


app: FastAPI = create_app(settings)

app.mount("/static", StaticFiles(directory="views/static"), name="static")

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Custom title",
        version="2.5.0",
        description="This is a very custom OpenAPI schema",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

app = get_app_for_applied_routes(app)

handler = Mangum(app)
