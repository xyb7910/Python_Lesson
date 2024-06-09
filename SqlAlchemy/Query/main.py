from sqlalchemy import func
from sqlalchemy.orm import sessionmaker

from SqlAlchemy.LinkDB.main import engine
from SqlAlchemy.Model.main import User

# 创建 session 对象
session = sessionmaker(bind=engine)()

# 参数为 模型名 -- 全表查询
# users = session.query(User).all()
# for user in users:
#     print(user)

# 参数为 模型名中的属性 -- 返回对应的数据
# users_name = session.query(User.name).all()
# for user_name in users_name:
#     print(user_name)

# 参数为 mysql 聚合函数
# 查询用户的数量
users_sum = session.query(func.count(User.id)).first()
print(users_sum)
'''
输出结果为：(2,)
'''
# 查询所有用户年龄的平均值
users_age_avg = session.query(func.avg(User.age)).first()
print(users_age_avg)
'''
输出结果为：(Decimal('20.0000'),)
'''
# 查询所有用户中最大的年龄
user_max_age_name = session.query(func.max(User.age)).first()
print(user_max_age_name)
'''
输出结果为：(22,)
'''
# 查询所有用户中年龄最大的人的姓名
user_max_age = session.query(func.max(User.age)).scalar()
print(user_max_age)
user_max_age_name = session.query(User.name).filter(User.age == user_max_age).first()
print(user_max_age_name[0])
'''
输出结果为：
22
yxc
'''
# 查询出年龄低于平均年龄的用户名
user_avg_age = session.query(func.max(User.age)).scalar()
user_age_less_than_avg_age_name = session.query(User.name).filter(User.age < user_avg_age).scalar()
print(user_age_less_than_avg_age_name)
'''
输出结果为：ypb
'''