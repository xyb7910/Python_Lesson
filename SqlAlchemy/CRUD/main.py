from sqlalchemy.orm import sessionmaker

from SqlAlchemy.LinkDB.main import engine
from SqlAlchemy.Model.main import User

# 构建 session 对象
session = sessionmaker(bind=engine)()

# 添加一个对象
# 创建一个对象
p1 = User(name='ypb', age=18)
# 将对象添加到 session 会话对象中
# session.add(p1)
# 将 session 中的对象做 commit（提交）
# session.commit()

# 一次性添加多个对象
p2 = User(name='zmz', age=19)
p3 = User(name='yxc', age=22)
# session.add_all([p2, p3])
# session.commit()

# 查找对象

# 查找某个模型对应的那个表中所有的数据
# all_users = session.query(User).all()
# for user in all_users:
#     print(user)
'''
    print(user) 输出的内容：
    <SqlAlchemy.Model.main.User object at 0x104b1c2e0>
    <SqlAlchemy.Model.main.User object at 0x104b1c340>
    <SqlAlchemy.Model.main.User object at 0x104b1c220>
'''
# filter_by 进行条件查询
# all_users = session.query(User).filter_by(age=18).all()
# for user in all_users:
#     print(user)

# filter 进行 条件查询
# all_users = session.query(User).filter(User.age == 18).all()
# for user in all_users:
#     print(user)


# 使用 get 方法查找数据, 根据主键进行查找
# user = session.query(User).get(1)
# user = session.get(User, 1)
# print(user)


# 使用 first 返回表中的第一条数据
# user = session.query(User).first()
# print(user)

# 修改对象
# user = session.query(User).filter_by(name='zmz').all()
# for u in user:
#     u.age = 19
# session.commit()


# 删除对象
# user = session.query(User).filter_by(name='zmz').first()
# if user is not None:
#     session.delete(user)
#     session.commit()

session.close()
