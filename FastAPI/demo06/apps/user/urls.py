from fastapi import APIRouter, Form

from FastAPI.demo05.apps.user.urls import User

user = APIRouter()


class User:
    username: str
    password: str
    re_password: str


@user.post("/register")
async def register_user(
        username: str = Form(min_length=3, max_length=6),
        password: str = Form(),
        re_password: str = Form()):
    if password != re_password:
        return {
            "status": False,
        }
    else:
        return {
            "status": True,
            "username": username,
            "password": password,
            "re_password": re_password
        }
