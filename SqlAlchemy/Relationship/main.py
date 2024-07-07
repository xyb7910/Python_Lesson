from tkinter import Text

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

from SqlAlchemy.LinkDB.main import engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    uname = Column(String(50), nullable=False)

    def __repr__(self):
        return "<User(uname='%s')>" % (self.uname)


class News(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    content = Column(String(1000), nullable=False)
    # 外键
    uid = Column(Integer, ForeignKey('user.id'), nullable=False)

    author = relationship("User", backref="news")

    def __repr__(self):
        return "<News(title='%s' content='%s')>" % (self.title, str(self.content))


# Base.metadata.create_all(engine)

# 插入模拟数据

# 新建 session
session = sessionmaker(bind=engine)()

# 新建一个 User
# p1 = User(uname='ypb')
# new1 = News(title='Java为何如此有趣', content='这是一篇关于介绍java为什么有趣的文章', uid=p1.id)
# new2 = News(title='Go语言如此美妙', content='我爱Go语言', uid=p1.id)
# session.add_all([p1, new1, new2])
#
# p2 = User(uname='yxc')
# new3 = News(title='Python太难啦', content='这是一片哭爹喊娘的Python自救文章', uid=p2.id)
# new4 = News(title='C++', content='C++测试型文章', uid=p2.id)
# session.add_all([p2, new3, new4])
# session.commit()


# 需求1：查询第一篇新闻的作者名
'''
news = session.query(News).first()
print(news)
print(news.uid)
user = session.query(User).get(news.uid)
print(user.uname)

# 引入了 relationship 进行查询优化
news = session.query(News).first()
print(news.author.uname)
'''

# 需求2: 查询某个作者的所有文章
'''
author = session.query(User).filter_by(uname='yxc').first()
print(author.news)
'''

# 需求3:使用 relationship 进行插入优化
'''
p3 = User(uname='zmz')
print(type(p3.news))
p3.news = [News(title='测试relationship', content='这是一篇测试relationship增加数据的文章', uid=p3.id)]
session.add(p3)
session.commit()
'''

# 需求4: 使用relationship 进行反向插入
'''
p4 = User(uname='gll')
new5 = News(title='测试relationship反向插入', content='这是一篇测试relationship反向插入数据的文章', author=p4)
session.add(new5)
session.commit()
'''


