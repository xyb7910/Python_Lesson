from fastapi import APIRouter

shop = APIRouter()


@shop.get('/')
async def index():
    return "This is shop index"


@shop.get('/{id}')
async def get_shop_by_id(id: int):
    return {'shop': 'shop', 'id': id}
