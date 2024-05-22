from fastapi import APIRouter, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

user = APIRouter()
user.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@user.get("/", response_class=HTMLResponse, tags=["用户主页面"])
async def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html", context={
        "username": 'yxc',
        "age": 18,
    })
