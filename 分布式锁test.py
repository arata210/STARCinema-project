import time
from redis import Redis


class DistributedLock:
    def __init__(self, redis_conn, lock_key, expiration_time=10):
        self.redis_conn = redis_conn
        self.lock_key = lock_key
        self.expiration_time = expiration_time
        self.lock_value = None

    def acquire_lock(self):
        # 生成唯一的锁值
        self.lock_value = str(time.time())

        # 尝试获取锁，设置锁的超时时间
        result = self.redis_conn.set(self.lock_key, self.lock_value, nx=True, ex=self.expiration_time)

        return result is not None

    def release_lock(self):
        # 释放锁，确保只有持有锁的客户端才能释放它
        if self.redis_conn.get(self.lock_key) == self.lock_value:
            self.redis_conn.delete(self.lock_key)


# 使用你提供的 Redis 连接信息
redis_host = '192.168.88.130'
redis_port = 6379
redis_password = '123456'

# 连接到 Redis 服务器
redis_conn = Redis(host=redis_host, port=redis_port, decode_responses=True, password=redis_password)

# 创建分布式锁实例
lock_key = 'movie_seat_lock'
distributed_lock = DistributedLock(redis_conn, lock_key)

# 尝试获取分布式锁
if distributed_lock.acquire_lock():
    try:
        # 在这里执行需要保护的代码，例如更新座位状态的操作
        print("Lock acquired. Performing protected operations...")

    finally:
        # 释放分布式锁
        distributed_lock.release_lock()
        time.sleep(10)
        print("Lock released.")

else:
    print("Failed to acquire lock. Another process may have it.")
