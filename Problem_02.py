"""
第 0002 题: 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
数据库名称：MySQL
密码：root 
"""

import pymysql
import string
import random

class MyDb():
    def __init__(self):
        self.conn = None

    def connect( self ):
        self.conn =  pymysql.connect(
            host = "localhost",             
            user = "13399132667", 
            password= "h654321.0",
            port = 3306,
            db = 'houlinjie'
            )

    def cursor( self ):
        return self.conn.cursor()

    def commit( self ):
        return self.conn.commit()

    def close( self ):
        return self.conn.close()


def DropTable(conn):
    conn.execute("DROP TABLE IF EXISTS PC_table")

def CreateTable(conn):
    sql_create = """CREATE TABLE PC_table (
        PC_id int not null auto_increment,
        PC varchar(255),
        primary key(PC_id)
        ) """
    conn.execute(sql_create)

def InsertDatas(conn, PCs):
    insert_sql = "INSERT INTO PC_table (PC) VALUES (%s)"
    conn.executemany(insert_sql, PCs)

def QueryData(conn):
    sql = "select * from pc_table"
    conn.execute(sql)
    rows = conn.fetchall()
    if rows is None:
        print("rows None")
    for row in rows:
        print(row)

def gen_key(num, len=16, base_str = string.ascii_letters + string.digits):  # num 为生成多少个，len 每个的长度
    result = []
    for i in range(num):  #控制生成多少个
        key_list = [random.choice(base_str) for i in range(len)]  #用列表生成式生成列表
        key_str = ''.join(key_list)         # 将列表用join形成字符串
        result.append(key_str)
    return result

if __name__ == '__main__':
    db = MyDb()
    db.connect()  
    cursor = db.cursor()
    DropTable(cursor)
    CreateTable(cursor)

    PC_s = gen_key(200)
    InsertDatas(cursor, PC_s)
    db.commit()
    QueryData(cursor)
    db.close()









