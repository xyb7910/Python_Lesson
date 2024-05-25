from sqlalchemy import insert, delete, select
from FastAichemy.learn.table import user_table, address_table, engine

# 单条执行插入语句
'''
# 插入语句
ins = user_table.insert().values(name='zhang', fullname='xin')
print(ins.compile().params)

# 执行
conn = engine.connect()
result = conn.execute(ins)
'''

# 多条执行插入语句
'''
ins = user_table.insert()
conn = engine.connect()
# conn.execute(ins, {"name": "zhang", "fullname": "xin"})
conn.execute(ins, [
        {'name': 'li', 'fullname': 'ming'},
        {'name': 'yao', 'fullname': 'zhetian'},
        {'name': 'fan', 'fullname': 'sixian'},
])
conn.commit()
'''

# 无条件选择整表数据
'''
s = select(user_table)
conn = engine.connect()
result = conn.execute(s)
result = result.fetchall()
for row in result:
    print(row)
'''

# 选择特定列数据
'''
s = select(user_table.c.fullname)
conn = engine.connect()
result = conn.execute(s)
for row in result:
    print(row)
'''
