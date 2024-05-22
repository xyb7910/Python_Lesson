import uvicorn
from fastapi import FastAPI
from FastAPI.demo10.model.models import LoginModel
from tortoise.contrib.fastapi import register_tortoise
from config import db


app = FastAPI()
register_tortoise(
    app=app,
    config=db.TORTOISE_ORM,
)


# 查询所有数据
@app.get("/queryall", description="查询所有用户信息")
async def queryall():
    elements = await LoginModel.all()
    for u in elements:
        print(u)  # <LoginModel>
    return {
        "data": elements,
    }


# 过滤查询 filter

# 获取第一条数据 first
@app.get("/getfirst", description="获取第一条数据信息")
async def getfirst():
    element = await LoginModel.first()
    print(element)
    return {
        "data": element,
        "message": "Get First Successfully"
    }


# 获取指定信息的数据
@app.get("/getinfo")
async def getinfo(id: int):
    element = await LoginModel.get(id=id)
    print(element)
    return {
        "data": element,
        "message": "Get First Successfully"
    }


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000, log_level="debug")
