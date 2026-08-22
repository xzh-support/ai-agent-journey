# 入口：TODO API 全部路由
import json

import pymysql
from fastapi import Depends, FastAPI, HTTPException

from app.auth import create_token, get_current_user, hash_password, verify_password
from app.db import cache_delete, cache_get, cache_set, get_conn
from app.schemas import LoginIn, RegisterIn, TodoIn, TodoUpdate

app = FastAPI(title="TODO API", description="综合项目：FastAPI + MySQL + Redis + JWT")


# ============ 注册 / 登录 ============
@app.post("/register", status_code=201)
def register(body: RegisterIn):
    """注册：数据库里存的是加盐哈希，绝不存明文（面试考点）"""
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO users (username, password_hash) VALUES (%s, %s)",
                (body.username, hash_password(body.password)),
            )
            conn.commit()
            return {"id": cur.lastrowid, "username": body.username}
    except pymysql.IntegrityError:
        # 唯一索引兜底：两个同名请求同时注册，数据库会拒绝后一个
        raise HTTPException(status_code=400, detail="用户名已存在")
    finally:
        conn.close()


@app.post("/login")
def login(body: LoginIn):
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, username, password_hash FROM users WHERE username = %s",
                (body.username,),
            )
            row = cur.fetchone()
            # 用户不存在和密码错误返回同一个提示：不泄露"哪个错了"
            if row is None or not verify_password(body.password, row["password_hash"]):
                raise HTTPException(status_code=401, detail="用户名或密码错误")
            return {"token": create_token(row["id"], row["username"])}
    finally:
        conn.close()


# ============ TODO 增删改查（全部需要登录）============
def todo_key(user_id: int) -> str:
    """每个用户的缓存 key 都带自己的 id，互不串数据"""
    return f"todos:{user_id}"


@app.get("/todos")
def list_todos(user: dict = Depends(get_current_user)):
    """查自己的 TODO：先看 Redis，没有才查 MySQL（缓存旁路模式）"""
    key = todo_key(user["user_id"])

    cached = cache_get(key)
    if cached is not None:
        return {"todos": json.loads(cached), "来源": "Redis 缓存"}

    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, title, done, created_at FROM todos "
                "WHERE user_id = %s ORDER BY id DESC",
                (user["user_id"],),
            )
            todos = cur.fetchall()
    finally:
        conn.close()

    cache_set(key, json.dumps(todos, default=str), ex=60)  # default=str 处理 datetime
    return {"todos": todos, "来源": "MySQL"}


@app.post("/todos", status_code=201)
def create_todo(body: TodoIn, user: dict = Depends(get_current_user)):
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO todos (user_id, title) VALUES (%s, %s)",
                (user["user_id"], body.title),
            )
            conn.commit()
            todo_id = cur.lastrowid
    finally:
        conn.close()

    cache_delete(todo_key(user["user_id"]))   # 数据变了，缓存作废
    return {"id": todo_id, "title": body.title, "done": False}


@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, body: TodoUpdate, user: dict = Depends(get_current_user)):
    """部分更新：传 title 就改 title，传 done 就改 done"""
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            # 先确认这条 TODO 存在且属于自己（防止水平越权，面试考点）
            cur.execute(
                "SELECT id FROM todos WHERE id = %s AND user_id = %s",
                (todo_id, user["user_id"]),
            )
            if cur.fetchone() is None:
                raise HTTPException(status_code=404, detail="TODO 不存在")

            # 动态拼 SET 子句：f-string 里拼的是我们写死的列名，不是用户输入，安全
            fields, values = [], []
            if body.title is not None:
                fields.append("title = %s")
                values.append(body.title)
            if body.done is not None:
                fields.append("done = %s")
                values.append(body.done)
            if not fields:
                raise HTTPException(status_code=400, detail="没有需要修改的内容")

            values.append(todo_id)
            cur.execute(f"UPDATE todos SET {', '.join(fields)} WHERE id = %s", values)
            conn.commit()
    finally:
        conn.close()

    cache_delete(todo_key(user["user_id"]))
    return {"message": "已更新"}


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, user: dict = Depends(get_current_user)):
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            # DELETE 没删掉东西 rowcount 一定是 0，可以放心直接判断
            cur.execute(
                "DELETE FROM todos WHERE id = %s AND user_id = %s",
                (todo_id, user["user_id"]),
            )
            conn.commit()
            if cur.rowcount == 0:
                raise HTTPException(status_code=404, detail="TODO 不存在")
    finally:
        conn.close()

    cache_delete(todo_key(user["user_id"]))
    return {"message": "已删除"}
