# 查询参数 + Pydantic 请求体
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# ============ 1. 查询参数：URL 问号后面的东西 ============
@app.get("/items")
def list_items(limit: int = 10, keyword: str = ""):
    """GET /items?limit=5&keyword=书 这种请求，参数自动解析"""
    return {
        "limit": limit,        # ?limit=5   → 5
        "keyword": keyword,    # ?keyword=书 → "书"
        "说明": "limit 有默认值 10，不传就用 10"
    }


# ============ 2. Pydantic 请求体：POST 的 body ============
class ChatRequest(BaseModel):      # 继承 BaseModel = 定义"请求体长什么样"
    message: str                   # 必填字段：字符串
    max_tokens: int = 100          # 可选字段：默认 100
    temperature: float = 0.7       # 可选字段：默认 0.7


@app.post("/chat")
def chat(req: ChatRequest):        # 参数声明为 ChatRequest 类型
    """POST /chat，body 是 JSON，FastAPI 自动解析 + 校验 + 转成 ChatRequest 对象"""
    return {
        "收到消息": req.message,
        "参数": {
            "max_tokens": req.max_tokens,
            "temperature": req.temperature,
        }
    }
