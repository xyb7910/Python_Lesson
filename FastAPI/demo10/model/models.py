from tortoise.models import Model
from tortoise import fields


class LoginModel(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=100, description="用户名")
    password = fields.CharField(max_length=100, description="密码")
    re_password = fields.CharField(max_length=100, description="重复密码")
    phone_number = fields.CharField(max_length=100, description="手机号")


class LessonModel(Model):
    id = fields.IntField(pk=True)
    lesson_name = fields.CharField(max_length=100, description="课程名字")
    lesson_desc = fields.CharField(max_length=100, description="课程描述")
    lesson_room = fields.CharField(max_length=100, description="上课教师")
