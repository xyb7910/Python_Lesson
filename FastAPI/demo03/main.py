from enum import Enum

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from apps.shop.urls import shop

app = FastAPI()

app.include_router(shop, prefix="/shop", tags=[" This is shop api"])


class PeopleRole(str, Enum):
    admin = "admin"
    user = "user"


@app.get("/api/{people_roler}")
async def get_people_role(people_roler: PeopleRole):
    if people_roler is PeopleRole.admin:
        return PeopleRole.admin
    elif people_roler.value == "user":
        return PeopleRole.user
    else:
        return "Not found"


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug")
