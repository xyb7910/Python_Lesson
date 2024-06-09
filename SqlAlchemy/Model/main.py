from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

from SqlAlchemy.LinkDB.main import engine

Base = declarative_base()


# 定义自己的类
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

    # 重写 __repr__ 实现打印数据库数据
    def __repr__(self):
        return f"<User(name={self.name}, age={self.age})>"


# 建立与数据库的映射
Base.metadata.create_all(engine)

# 删除与数据库的映射
# Base.metadata.drop_all(engine)
