from fastapi import APIRouter, Query
from typing import Union

user = APIRouter()


@user.get("/")
def index():
    return "This is user index"


@user.get("/info")
def getUserInfo(id: int, username: str):
    return {
        "id": id,
        "username": username,
        "message": "Get user information success",
    }


#  支持多个路径参数和查询参数
@user.get("/articles/{user_id}/items/{item_id}")
def getUserItem(user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item["q"] = q
    if not short:
        item.update({"short": True})
    return item


# 请求参数值的设定 -- 提供article_id == 0的默认值
@user.get("/articles")
def getUserArticles(user_id: int, article_id: int = 0):
    return {
        "articles": article_id,
        "user_id": user_id,
    }


# 需求：查询user编写的文章，最大的文章id限定在3到5之间
@user.get("/articles_id")
def getUserArticlesByID(user_id: int, article_id: Union[str, None] = Query(default=None, max_length=5, min_length=3)):
    if len(article_id) > 5:
        return {
            "articles": article_id,
            "user_id": user_id,
            "message": "Get articles failed, because article_id is too long",
        }
    elif len(article_id) < 3:
        return {
            "articles": article_id,
            "user_id": user_id,
            "message": "Get articles failed, because article_id is too short",
        }
    else:
        return {
            "articles": article_id,
            "user_id": user_id,
            "message": "GetArticleById articles success",
        }

