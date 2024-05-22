from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `loginmodel` ADD `phone_number` VARCHAR(100) NOT NULL  COMMENT '手机号';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `loginmodel` DROP COLUMN `phone_number`;"""
