import string
import random

from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.elements import and_
from sqlalchemy.testing import in_
from sqlalchemy import not_, or_
from SqlAlchemy.LinkDB.main import engine
from SqlAlchemy.Model.main import User

# 创建 session 对象
session = sessionmaker(bind=engine)()

# 本地生成mock数据
'''
for i in range(6):
    # 生成随机名字, 长度为4到7个字符
    name = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(4, 7)))
    # 生成随机年龄, 范围为20到40
    age = random.randint(20, 40)
    user = User(name=name, age=age)
    # print(user.name, user.age)
    session.add(user)
    session.commit()
'''

# ==
user = session.query(User).filter(User.age == 21).all()
print(user)
'''
输出结果：[<User(name=KOBND, age=21)>]
'''

# ！=
users = session.query(User).filter(User.age != 40).all()
for user in users:
    print(user)

'''
输出结果：
<User(name=ypb, age=18)>
<User(name=yxc, age=22)>
<User(name=wwQE, age=23)>
<User(name=nzUjld, age=36)>
<User(name=uzjcgd, age=38)>
<User(name=Kbvifw, age=27)>
<User(name=KOBND, age=21)>
'''

# like
users = session.query(User).filter(User.name.like('y%')).all()
for user in users:
    print(user)

'''
输出结果：
<User(name=ypb, age=18)>
<User(name=yxc, age=22)>
'''

# ilike （对大小写不敏感）
users = session.query(User).filter(User.name.ilike('y%')).all()
for user in users:
    print(user)
'''
输出结果：
<User(name=ypb, age=18)>
<User(name=yxc, age=22)>
'''

# in
users = session.query(User).filter(User.age.in_(range(18, 30))).all()
for user in users:
    print(user)
'''
输出结果：
<User(name=ypb, age=18)>
<User(name=yxc, age=22)>
<User(name=wwQE, age=23)>
<User(name=Kbvifw, age=27)>
<User(name=KOBND, age=21)>
'''

# not in
# 第一种写法
users = session.query(User).filter(not_(User.age.in_(range(18, 30))))
# 第二种写法
users = session.query(User).filter(~(User.age.in_(range(18, 30))))
for user in users:
    print(user)
'''
输出结果：
<User(name=RPIaXC, age=40)>
<User(name=nzUjld, age=36)>
<User(name=uzjcgd, age=38)>
'''

# is null
# 第一种写法
user = session.query(User).filter(User.age == None).all()
# 第二种写法
user = session.query(User).filter(User.age.is_(None)).all()
print(user)
'''
输出结果：[]
'''

# is not null
# 第一种写法
users = session.query(User).filter(User.name != None).all()
# 第二种写法
users = session.query(User).filter(User.name.isnot(None)).all()
for user in users:
    print(user)
'''
输出结果：
<User(name=ypb, age=18)>
<User(name=yxc, age=22)>
<User(name=wwQE, age=23)>
<User(name=RPIaXC, age=40)>
<User(name=nzUjld, age=36)>
<User(name=uzjcgd, age=38)>
<User(name=Kbvifw, age=27)>
<User(name=KOBND, age=21)>
'''

# and
# 第一种写法
user = session.query(User).filter(and_(User.name == 'ypb',User.age == 18)).first()
# 第二种写法
user = session.query(User).filter(User.name == 'ypb',User.age == 18).first()
# 第三种写法
user = session.query(User).filter(User.name == 'ypb').filter(User.age == 18).first()

print(user)
'''
输出结果：<User(name=ypb, age=18)>
'''

# or
users = session.query(User).filter(or_(User.age <= 20, User.age >= 30)).all()
for user in users:
    print(user)
'''
输出结果：
<User(name=ypb, age=18)>
<User(name=RPIaXC, age=40)>
<User(name=nzUjld, age=36)>
<User(name=uzjcgd, age=38)>
'''