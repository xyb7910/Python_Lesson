import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_active: bool

@app.get("/")
def index():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
def item_id(item_id: int):
    return {"item_id": item_id}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "item": item}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug", reload=True)
