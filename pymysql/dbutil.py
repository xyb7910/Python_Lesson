import pymysql


class dbUtil:
    config = {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': '123456789',
        'database': 'tortoise',
        'charset': 'utf8'
    }

    def __init__(self):
        self.conn = pymysql.connect(**dbUtil.config)
        self.cur = self.conn.cursor()

    def close(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()

    def exeDML(self, sql, *args):
        try:
            count = self.cur.execute(sql, args)
            self.conn.commit()
            return count
        except Exception as e:
            print(e)
            if self.conn:
                self.conn.rollback()
        finally:
            self.close()

    def query_one(self, sql, *args):
        try:
            self.cur.execute(sql, args)
            res = self.cur.fetchone()
            return res
        except Exception as e:
            print(e)
            if self.conn:
                self.conn.rollback()
        finally:
            self.close()

    def query_all(self, sql, *args):
        try:
            self.cur.execute(sql, args)
            res = self.cur.fetchall()
            return res
        except Exception as e:
            print(e)
            if self.conn:
                self.conn.rollback()
        finally:
            self.close()


if __name__ == '__main__':
    dbUtil = dbUtil()
    # 测试插入
    '''
    sql = 'insert into user_account(name, fullname) values (%s, %s)'
    cnt = dbUtil.exeDML(sql, "test_name", "test_fullname")
    print(cnt)
    '''

    # 测试单条查询
    '''
    sql = "select name, fullname from user_account where id = %s"
    cnt = dbUtil.query_one(sql, 17)
    print(cnt)
    '''

    # 测试多条查询
    '''
    sql = "select name, fullname from user_account"
    res = dbUtil.query_all(sql)
    for row in res:
        print(row)
    '''
