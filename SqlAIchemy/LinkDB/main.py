from sqlalchemy import create_engine, text

SQLALCHEMY_DATABASE_URL = "mysql://root:123456789@127.0.0.1:3306/tortoise"

# 创建数据库引擎
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)

# 创建连接
'''
with engine.connect() as connection:
    rs = connection.execute(text('select * from user_account'))
    print(rs)
    res = rs.fetchall()
    for r in res:
        print(r)
'''
