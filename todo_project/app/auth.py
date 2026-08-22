# 注册登录相关：密码加盐哈希 + JWT 签发/校验
import hashlib
import os
import secrets
from datetime import datetime, timedelta, timezone

import jwt
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

SECRET_KEY = os.getenv("SECRET_KEY", "my-secret-key-2026")
ALGORITHM = "HS256"


def hash_password(password: str, salt: str = None) -> str:
    """加盐哈希，存成 "盐$哈希" 格式。
    盐是随机生成的，两个密码相同的人哈希也不一样（防彩虹表）"""
    if salt is None:
        salt = secrets.token_hex(16)          # 32 位随机十六进制
    digest = hashlib.sha256((salt + password).encode("utf-8")).hexdigest()
    return f"{salt}${digest}"


def verify_password(password: str, stored: str) -> bool:
    salt, _, _ = stored.partition("$")
    return hash_password(password, salt) == stored


def create_token(user_id: int, username: str) -> str:
    """登录成功后签发 token：用户 id 放进 payload"""
    return jwt.encode(
        {
            "sub": str(user_id),
            "username": username,
            "exp": datetime.now(timezone.utc) + timedelta(hours=2),
        },
        SECRET_KEY,
        algorithm=ALGORITHM,
    )


security = HTTPBearer(auto_error=False)  # 声明 Bearer 安全方案 → /docs 出现 Authorize 按钮和锁图标


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> dict:
    """FastAPI 依赖：解析 Bearer token，返回 {"user_id", "username"}"""
    if credentials is None:  # auto_error=False：没带 Authorization 头时是 None，由我们自己返回 401
        raise HTTPException(status_code=401, detail="未登录")

    try:
        # HTTPBearer 已帮我们拆好 "Bearer " 前缀，credentials.credentials 就是纯 token
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="token 已过期，请重新登录")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="token 无效")

    return {"user_id": int(payload["sub"]), "username": payload["username"]}
