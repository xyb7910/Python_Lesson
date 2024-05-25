from sqlalchemy import Column, Table, Integer, String, ForeignKey
from sqlalchemy import MetaData
from sqlalchemy import create_engine

metadata_obj = MetaData()

user_table = Table(
    "user_account",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(30)),
    Column("fullname", String(30)),
)

'''
print(user_table.c.name)
print(user_table.c.keys())
'''
address_table = Table(
    "address_account",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("user_account.id"), nullable=False),
    Column("address", String, nullable=False),
)

SQLALCHEMY_DATABASE_URL = "mysql://root:123456789@127.0.0.1:3306/tortoise"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True,
    future=True,
)

metadata_obj.create_all(engine)
