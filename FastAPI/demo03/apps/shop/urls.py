from fastapi import APIRouter

shop = APIRouter()


@shop.get('/')
async def index():
    return "This is index"


@shop.get('/detail/{id}')
def detail(id):
    print("获取购物详情的id的类型为 %s" % type(id))
    return {
        "id": id,
        "message": "Get detail ok"
    }
