import pymysql
conn = None
cur = None
try:
    # 获取连接对象
    conn = pymysql.connect(host='localhost', password='123456789', user='root', db='tortoise')
    print(conn)
    # 创建 cursor
    cur = conn.cursor()
    # 编写sql
    # 查询全部
    # sql = 'select * from user_account'
    # 插入语句
    # sql = "insert into user_account(name, fullname) values('yan', 'yanpengbo')"
    # 修改语句
    # sql = "update user_account set fullname='minxing' where id=3"
    # 删除语句
    # sql = "delete from user_account where id = 3"
    # 规避查询漏洞
    # sql = "select * from user_account where id=%s"
    # 新增
    sql = "insert into user_account(name, fullname) values (%s, %s)"
    # 执行sql
    args =("zhang", "xiaoming")
    cnt = cur.execute(sql,args)
    # 查看结果集
    '''
    cmp = cur.fetchall()
    for row in cmp:
        print(row)
    '''
    print(cnt)
    # 执行DML
    conn.commit()
except Exception as e:
    print(e)
    if conn:
        conn.rollback()
finally:
    if cur:
        cur.close()
    if conn:
        conn.close()