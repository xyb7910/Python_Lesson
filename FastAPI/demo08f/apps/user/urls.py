from typing import Dict

from fastapi import APIRouter

user = APIRouter()


# 在路由请求中添加响应模型
@user.get('/getuserinfo', response_model=Dict[str, str])
async def get_user_info() -> Dict[str, str]:
    return {
        "username": "yxc",
        "age": '18',
        "address": "Shanxi"
    }
