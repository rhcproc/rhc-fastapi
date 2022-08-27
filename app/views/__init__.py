from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from settings import settings, BASE_DIR

template_engine = Jinja2Templates(
    directory=f"{BASE_DIR}/views/templates")
templating = template_engine.TemplateResponse
