from fastapi import FastAPI
import uvicorn
from apps.user.urls import user

app = FastAPI()

app.include_router(user, prefix="/user", tags=["user"])

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug")
