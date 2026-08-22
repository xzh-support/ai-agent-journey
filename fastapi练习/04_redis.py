# FastAPI + Redis：对话历史 + 缓存计数器
import redis
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 连接本地 Redis 容器（6380 端口是启动时映射的）
r = redis.Redis(host="localhost", port=6380, decode_responses=True)
#                                          ↑ 自动把字节解码成字符串，中文不乱码


# ============ 1. 模拟"对话历史"：List 的实战 ============
class ChatMessage(BaseModel):
    user: str
    text: str


@app.post("/chat-history")
def add_message(msg: ChatMessage):
    """用户发一条消息，LPUSH 进 Redis 列表"""
    r.lpush(f"chat:{msg.user}", msg.text)          # 最新消息在最前
    r.ltrim(f"chat:{msg.user}", 0, 9)              # 只保留最近 10 条
    return {"status": "已保存"}


@app.get("/chat-history/{user}")
def get_history(user: str, limit: int = 10):
    """取最近 N 条对话（LRANGE），返回顺序翻转成时间正序"""
    msgs = r.lrange(f"chat:{user}", 0, limit - 1)
    return {"user": user, "history": msgs[::-1]}   # 切片反转 = 旧的在前


# ============ 2. 接口计数器：String 的实战 ============
@app.get("/stats")
def visit_stats():
    """每次访问计数 +1（INCR 原子自增，并发安全）"""
    total = r.incr("total_visits")
    return {"总访问次数": total}
