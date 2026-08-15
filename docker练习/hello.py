# 一个极简网页服务器，用 Python 自带模块，不需要装任何包
from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write("你好，我是跑在容器里的 Python 程序！".encode("utf-8"))

HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
