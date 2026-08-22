# 第一个 FastAPI 应用
from fastapi import FastAPI

app = FastAPI()          # 创建应用实例（整个项目的"入口"）


@app.get("/")            # 装饰器：声明"GET 请求访问 / 时，执行下面这个函数"
def hello():
    return {"message": "你好，FastAPI！"}


@app.get("/hello/{name}")   # 路径参数：URL 里 {} 包住的部分会传给函数
def hello_name(name: str):
    return {"message": f"你好，{name}！"}
