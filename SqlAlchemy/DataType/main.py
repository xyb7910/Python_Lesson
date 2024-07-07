import datetime
import enum

from sqlalchemy import Column, Integer, String, Boolean, Enum, DateTime, Date, Time, Text
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from SqlAlchemy.LinkDB.main import engine

Base = declarative_base()


# 定义一个枚举类
class TagEnum(enum.Enum):
    python = 'python',
    java = 'java',
    c = 'c',
    javascript = 'javascript',
    cpp = 'cpp',


class News(Base):
    __tablename__ = 'news'
    # id 整数类型，限制主键自增
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 标题 长度为 100 字符类型， 不能为空
    title = Column(String(100), nullable=False)
    # 作者电话 字符类型 唯一
    author_telephone = Column(String(11), unique=True, nullable=False)
    # 是否删除 整型，不能为空， 默认为 0
    is_delete = Column(Integer, nullable=False, default=0)
    # 是否公开 布尔类型， 不能为空， 默认为 True
    is_published = Column(Boolean, nullable=False, default=True)
    # 标题1 枚举类型 常规写法
    tag1 = Column(Enum('python', 'java', 'go', 'javascript'))
    # 标题2 枚举类型 另一种写法
    tag2 = Column(Enum(TagEnum))
    # 时间的三种类型
    created_at = Column(Date, default=datetime.datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.datetime.now, default=datetime.datetime.now)
    published_at = Column(Time)
    # 文本的两种类型
    content1 = Column(Text)
    content2 = Column(LONGTEXT)


# 建立映射
Base.metadata.create_all(engine)
# Base.metadata.drop_all(engine)
# 新建一个会话对象
session = sessionmaker(bind=engine)()

# 创建一个 new 对象
new_demo = News(title='测试new',
                author_telephone='15991367893',
                is_delete=0,
                is_published=True,
                tag1='go',
                tag2=TagEnum.c,
                created_at=datetime.datetime.now(),
                updated_at=datetime.datetime.now(),
                published_at=datetime.time(),
                content1='这是一个测试性内容1',
                content2='这是一个测试性内容2')

# session.add(new_demo)
# session.commit()
# session.close()

# 测试 onupdate 参数
a_new = session.query(News).first()
a_new.title = '这是修改后的标题'
a_new.author_telephone = '15991367894'
# 提交事物
session.commit()
session.close()
