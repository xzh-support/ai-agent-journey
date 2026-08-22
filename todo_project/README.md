# TODO API 综合项目

FastAPI + MySQL + Redis + JWT + Docker —— 把第一阶段学的全部组装起来。

## 本地运行

1. 建表（只跑一次）：
   ```bash
   mysql -u root -p < setup.sql
   ```
2. 装依赖：
   ```bash
   pip install -r requirements.txt
   ```
3. 启动（必须在 todo_project 目录下）：
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```
4. 打开 http://127.0.0.1:8000/docs 开始测试

## Docker 运行

```bash
docker compose up -d --build
```

应用在 http://localhost:8000 ，MySQL 容器在 3307，Redis 容器在 6381。

## 测试流程

1. POST /register 注册
2. POST /login 拿 token（点右上角 Authorize 填 `Bearer <token>`）
3. POST /todos 创建两条 TODO
4. GET /todos —— 看"来源"字段：第一次 MySQL，60 秒内再查是 Redis 缓存
5. PUT /todos/{id} 把 done 改成 true
6. DELETE /todos/{id} 删掉一条
