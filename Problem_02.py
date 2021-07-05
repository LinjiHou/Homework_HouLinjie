"""
第 0002 题: 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
数据库名称：MySQL_HouLinjie
密码：123456

"""

import pymysql
import string
import random


class MyDb():
    def __init__(self):
        self.conn = None

    def connect( self ):
        # set parameters of MySQL
        self.conn =  pymysql.connect(
            host= "192.168.122.18", 
            port = 3306, 
            user = "mysql_houlinjie", 
            password= "123456", 
            db="active")

    def cursor( self ):
        try:
            return self.conn.cursor()
        except Exception:
            self.connect()
            return self.conn.cursor()

    def commit( self ):
        return self.conn.commit()

    def close( self ):
        return self.conn.close()


def DropTable(conn):
    conn.execute("DROP TABLE IF EXISTS `user_key`")

def CreateTable(conn):
    sql_create = ''' CREATE TABLE `user_key` (`key` varchar(50) NOT NULL)'''
    conn.execute(sql_create)

def InsertDatas(conn):
    insert_sql = "INSERT INTO user_key VALUES (%s)"
    key_list = gen_key(200)
    conn.executemany(insert_sql, key_list)

def QueryData(conn):
    sql = "select * from user_key"
    conn.execute(sql)
    rows = conn.fetchall()
    if rows is None:
        print("rows None")
    for row in rows:
        print(row)

def gen_key(num,len=7):  # num 为生成多少个，len 每个的长度
    result = []
    base_str = string.ascii_letters + string.digits    # 所有的大小写字母和数字
    for i in range(num):  #控制生成多少个
        key_list = [random.choice(base_str) for i in range(len)]  #用列表生成式生成列表
        # print(key_list)
        key_str = ''.join(key_list)         # 将列表用join形成字符串
        # print(key_str)
        result.append(key_str)
    return result

if __name__ == '__main__':
    db = MyDb()
    db.connect()
    cursor = db.cursor()
    DropTable(cursor)
    CreateTable(cursor)
    InsertDatas(cursor)
    db.commit()
    QueryData(cursor)
    db.close()









