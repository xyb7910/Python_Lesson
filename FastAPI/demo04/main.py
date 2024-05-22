import uvicorn
from fastapi import FastAPI
from apps.user.urls import user

app = FastAPI()

app.include_router(user, prefix="/user", tags=["This is user router"])

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug")