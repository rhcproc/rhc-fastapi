
from views import Request, APIRouter, templating, settings
import json
from fastapi import Form
from handlers.response import OK, CREATED
from settings import settings

api = APIRouter()

@api.get("/")
async def root(request: Request):
    return templating(
        'index.html',
        context={
            'request': request,
            'description': settings.description
        }
    )

@api.get(
    '/login',
    summary="Welcome",
    tags=['template'],
)
async def index(request: Request):
    """
    """
    return templating(
        'login.html',
        context={
            'request': request,
            'description': settings.description
        }
    )
