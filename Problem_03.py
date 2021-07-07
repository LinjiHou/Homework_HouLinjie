"""
第 0003 题： 将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。
需要先分别启动redis-server.exe服务端再启动redis-cli客户端。
"""
import redis
import string
import random

class MyRedis():
    def __init__(self):
        self.conn = None

    def connection( self ):
        self.conn = redis.Redis(
            host='127.0.0.1',
            port=6379,
            db=2)

    # 列表list　添加数据
    def lpush_redis( self ,k_list):
        for key in k_list:
            self.conn.lpush('key',key)

    # 集合set　添加数据
    def sadd_redis( self,k_list ):
        for key in k_list:
            self.conn.sadd('key',key)

    # 列表list　读取数据
    def lrange_redis( self ):
        k_list = self.conn.lrange('key',0,-1)
        for key in k_list:
            print(key.decode())

    # 集合set　读取数据
    def smembers_redis( self ):
        s = self.conn.smembers('key') #返回的是个集合set
        for key in s:
            print(key.decode())

    def flushdb_redis( self ):
        self.conn.flushdb()

def gen_key(num,len=16,base_str = string.ascii_letters + string.digits):  
    result = []
    for i in range(num):  #控制生成多少个
        key_list = [random.choice(base_str) for i in range(len)]  #用列表生成式生成列表
        key_str = ''.join(key_list)         # 将列表用join形成字符串
        result.append(key_str)
    return result

if __name__ == '__main__':
    r = MyRedis()
    r.connection()
    r.flushdb_redis()
    key_list = gen_key(200)
    # 列表list　　可以重复添加
    r.lpush_redis(key_list)
    r.lrange_redis()

    # 集合set（每个元素都是唯一，不能重复添加）　
    # r.sadd_redis(key_list)
    # r.smembers_redis()