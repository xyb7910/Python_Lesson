import uvicorn
from fastapi import FastAPI

from apps.user.urls import user
from apps.shop.urls import shop

app = FastAPI()

app.include_router(user, prefix="/user", tags=["This is user router"])
app.include_router(shop, prefix="/shop", tags=["This is shop router"])


@app.get("/")
async def root():
    return "This is root router"


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug")
