# 数据库与缓存连接：配置全部从环境变量读取，本地跑和 Docker 跑自动适配
import os
import pymysql
import redis

DB_CONFIG = {
    "host": os.getenv("MYSQL_HOST", "localhost"),
    "port": int(os.getenv("MYSQL_PORT", "3306")),
    "user": os.getenv("MYSQL_USER", "root"),
    "password": os.getenv("MYSQL_PASSWORD", "123456"),
    "database": os.getenv("MYSQL_DATABASE", "todo_db"),
    "charset": "utf8mb4",
    "cursorclass": pymysql.cursors.DictCursor,
}

# redis.Redis() 是懒连接：创建对象时不真正连，第一次使用时才连
r = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", "6380")),
    decode_responses=True,
)


def get_conn():
    """每次请求建立一条 MySQL 连接，用完关闭"""
    return pymysql.connect(**DB_CONFIG)


# ============ 缓存操作（带降级：Redis 挂了不影响主流程）============
def cache_get(key):
    """读缓存：Redis 出问题就当没缓存，走数据库（面试考点：缓存降级）"""
    try:
        return r.get(key)
    except redis.RedisError:
        return None


def cache_set(key, value, ex=60):
    try:
        r.set(key, value, ex=ex)
    except redis.RedisError:
        pass


def cache_delete(key):
    try:
        r.delete(key)
    except redis.RedisError:
        pass
