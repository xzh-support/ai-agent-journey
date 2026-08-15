# 基础镜像：带 Python 3.11 的迷你 Linux
FROM python:3.11

# 容器内的工作目录（没有会自动创建）
WORKDIR /app

# 把本地的 hello.py 复制到容器里的 /app 目录下
COPY hello.py .

# 容器启动时执行的命令
CMD ["python", "hello.py"]
