from fastapi import APIRouter, Path
from pydantic import BaseModel, Field
from typing import Union
from typing_extensions import Annotated

user = APIRouter()


@user.get('/')
def index():
    return 'This is index'


class Address(BaseModel):
    province: str
    city: str
    street: Union[str, None] = None


class User(BaseModel):
    id: int
    name: str
    age: int
    phone: str
    role: int
    address: Address


@user.post('/login')
def login(data: User):
    if data.role == 1:
        print("你是管理员")
    else:
        print("你是普通用户")
    return data


# 混合使用path，Query和请求体参数
class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@user.post('/items/{item_id}')
async def update_item(
        item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
        q: Union[str, None] = None,
        item: Union[Item, None] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results


class RegisterItem(BaseModel):
    username: str = Field(None, alias="username", max_length=50, min_length=3, description="这是用户的用户名配置")
    password: Union[str, None] = None
    re_password: Union[str, None] = None
    email: Union[str, None] = None
    phone: Union[str, None] = None


# 请求体中的字段
@user.post('/register')
def register(data: RegisterItem):
    return data
