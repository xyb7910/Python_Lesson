import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from apps.user.urls import user

app = FastAPI()
app.include_router(user, prefix="/user", tags=["user"])
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse, tags=["用户主页面"])
async def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html", context={
        "username": 'yxc',
        "age": 18,
    })


@app.get("/items/{id}",response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(request=request, name="index.html", context={
        "id": id
    })


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug")
