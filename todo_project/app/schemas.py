# 请求数据模型（Pydantic 负责校验，不符合规则自动返回 422）
from pydantic import BaseModel, Field


class RegisterIn(BaseModel):
    username: str = Field(min_length=2, max_length=20)
    password: str = Field(min_length=6, max_length=50)


class LoginIn(BaseModel):
    username: str
    password: str


class TodoIn(BaseModel):
    title: str = Field(min_length=1, max_length=200)


class TodoUpdate(BaseModel):
    """两个字段都可选：传哪个改哪个（部分更新）"""
    title: str | None = None
    done: bool | None = None
