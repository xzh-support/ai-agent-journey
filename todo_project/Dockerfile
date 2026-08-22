# 把应用打包成镜像
FROM python:3.11
WORKDIR /app
COPY requirements.txt .
# 国内加速用清华源（真实项目会锁定版本号，如 fastapi==0.115.0）
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
COPY app/ app/
# 0.0.0.0：容器里的服务必须监听所有网卡，宿主机才能访问
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
