from typing import List

from fastapi import APIRouter, UploadFile, File, Form
from starlette.responses import HTMLResponse

user = APIRouter()


@user.get('/index')
async def index():
    content = """
        <body>
        <form action="/user/byte_files" enctype="multipart/form-data" method="post">
        <input name="files" type="file" multiple>
        <input type="submit">
        </form>
        <form action="/user/upload_files" enctype="multipart/form-data" method="post">
        <input name="files" type="file" multiple>
        <input type="submit">
        </form>
        </body>
    """
    return HTMLResponse(content=content)


@user.post('/upload_file')
async def update_upload_file(file: UploadFile):
    return {
        "filename": file.filename,
    }


@user.post("/byte_file")
async def upload_file(file: bytes = File()):
    return {
        "file_length": len(file),
    }


@user.post("/update_cpp")
async def update_cpp(file: UploadFile):
    return {
        "file_name": file.filename,
        "file_content": await file.read(),
        "file_type": file.content_type,
        "message": "update cpp ok"
    }


# 上传多文件
@user.post("/byte_files")
async def upload_byte_files(files: List[bytes] = File(description="这是一个上传多个文件流的接口")):
    return {
        "files_length": [len(file) for file in files],
    }


@user.post("/upload_files")
async def upload_files(files: List[UploadFile] = File(description="这是一个上传多个UploadFile的接口")):
    return {
        "files_name": [file.filename for file in files],
    }


# Form & file 的混合使用
@user.post('/mutil')
async def update_mutil(
        file: bytes = File(description="这是混用中的上传文件流接口"),
        update_file: UploadFile = File(description="这是混用中的上传文件接口"),
        token: str = Form(description="这是混用中的表单获取接口")
):
    return {
        "file_size": len(file),
        "update_file_type": update_file.content_type,
        "token": token,
    }
