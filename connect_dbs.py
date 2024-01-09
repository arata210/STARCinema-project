from pymongo import MongoClient
from redis import Redis
import mysql.connector


class MongoDBConn:
    # 初始化 MongoDB 连接
    def __init__(self):
        # 获取数据库的连接
        self.client = MongoClient('192.168.88.130', 27017)


class RedisConn:
    # 初始化 Redis 连接
    def __init__(self):
        self.conn = Redis(host='192.168.88.130', port=6379, decode_responses=True, password='123456')


class MySQLConn:
    # 初始化 mysql 连接
    def __init__(self, host='localhost', user='root', password='123456', database='cinema'):
        # 初始化数据库连接
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        # 创建游标对象
        self.cursor = self.conn.cursor()

    def close_conn(self):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()

    def execute_query(self, query):
        # 执行查询
        self.cursor.execute(query)
        # 获取查询结果
        result = self.cursor.fetchall()
        return result

#
# Order = OrderManager("localhost", "root", "123456", "FilmOrder")
# print(Order)
# Order.close_connection()

