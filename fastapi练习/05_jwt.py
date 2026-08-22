# FastAPI + JWT：登录发 token，带 token 访问受保护接口
import jwt
from datetime import datetime, timedelta, timezone
from fastapi import FastAPI, Depends, HTTPException, Header
from pydantic import BaseModel

app = FastAPI()

SECRET_KEY = "my-secret-key-2026"   # 签名密钥（真实项目放环境变量，绝不提交到 git）
ALGORITHM = "HS256"                  # 签名算法


# ============ 1. 登录：验证密码，签发 token ============
# 模拟用户表（真实项目查数据库）
FAKE_USERS = {
    "alice": {"password": "123456", "role": "admin"},
    "bob": {"password": "123456", "role": "user"},
}


class LoginRequest(BaseModel):
    username: str
    password: str


@app.post("/login")
def login(req: LoginRequest):
    user = FAKE_USERS.get(req.username)
    if user is None or user["password"] != req.password:
        raise HTTPException(status_code=401, detail="用户名或密码错误")

    # 签发 JWT：payload 里放"身份信息"，设置过期时间
    token = jwt.encode(
        {
            "sub": req.username,              # subject：谁
            "role": user["role"],             # 自定义字段：角色
            "exp": datetime.now(timezone.utc) + timedelta(hours=1),  # 1小时后过期
        },
        SECRET_KEY,
        algorithm=ALGORITHM,
    )
    return {"token": token}


# ============ 2. 校验 token 的公共函数 ============
def get_current_user(authorization: str = Header(None)):
    """从请求头 Authorization 里解析 token，验签，返回用户信息"""
    if authorization is None:
        raise HTTPException(status_code=401, detail="未登录")

    scheme, _, token = authorization.partition(" ")
    # Authorization: Bearer eyJhbGci... → scheme="Bearer", token="eyJhbGci..."

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # decode = 验签 + 解出 payload；token 被篡改或过期都会抛异常
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="token 已过期，请重新登录")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="token 无效")

    return payload


# ============ 3. 受保护的接口：必须带合法 token ============
@app.get("/me")
def me(user: dict = Depends(get_current_user)):
    """Depends：FastAPI 自动先执行 get_current_user，结果注入 user 参数"""
    return {"用户名": user["sub"], "角色": user["role"]}


@app.get("/admin-only")
def admin_only(user: dict = Depends(get_current_user)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="需要管理员权限")
    return {"message": f"欢迎管理员 {user['sub']}"}
