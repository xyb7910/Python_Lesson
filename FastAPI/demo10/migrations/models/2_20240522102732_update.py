from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `lessonmodel` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `lesson_name` VARCHAR(100) NOT NULL  COMMENT '课程名字',
    `lesson_desc` VARCHAR(100) NOT NULL  COMMENT '课程描述',
    `lesson_room` VARCHAR(100) NOT NULL  COMMENT '上课教师'
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS `lessonmodel`;"""
