# FastAPI + MySQL：把数据库课的 students 表接进接口
import pymysql
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# 数据库连接配置（真实项目会放到配置文件/环境变量里）
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "123456",
    "database": "sql_practice",
    "charset": "utf8mb4",
    "cursorclass": pymysql.cursors.DictCursor,  # 查询结果返回字典而不是元组
}


def get_db():
    """每次请求建立一个连接，用完关闭"""
    return pymysql.connect(**DB_CONFIG)


# ============ 查：学生列表（含班级名，就是你练过的 LEFT JOIN）============
@app.get("/students")
def list_students():
    conn = get_db()
    try:
        with conn.cursor() as cur:      # with 自动管理游标
            cur.execute("""
                SELECT s.id, s.name, s.city, c.name AS class_name
                FROM students s
                LEFT JOIN classes c ON s.class_id = c.id
            """)
            return cur.fetchall()       # 直接返回列表+字典，FastAPI 自动转 JSON
    finally:
        conn.close()


# ============ 查：单个学生（路径参数）============
@app.get("/students/{student_id}")
def get_student(student_id: int):
    conn = get_db()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM students WHERE id = %s", (student_id,))
            #                                ↑ %s 是占位符，防 SQL 注入（面试考点！）
            row = cur.fetchone()
            if row is None:
                raise HTTPException(status_code=404, detail="学生不存在")
            return row
    finally:
        conn.close()


# ============ 增：新增学生（Pydantic 校验 + INSERT）============
class StudentIn(BaseModel):
    name: str
    class_id: int
    city: str


@app.post("/students", status_code=201)   # 201 = Created（创建成功）
def create_student(stu: StudentIn):
    conn = get_db()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO students (name, class_id, city) VALUES (%s, %s, %s)",
                (stu.name, stu.class_id, stu.city),
            )
            conn.commit()                 # 增删改必须 commit，否则不生效！
            return {"id": cur.lastrowid, **stu.model_dump()}
    finally:
        conn.close()
