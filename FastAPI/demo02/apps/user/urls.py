from fastapi import APIRouter

user = APIRouter()


@user.get('/')
def index():
    return "This is user index"


@user.get('/profile')
def profile():
    return "This is user profile"
