# 极简 HTTP 回显服务器：把收到的请求完整打印并返回
# 用途：学习 GET/POST 时，看"服务器视角"的请求长什么样
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json

class EchoHandler(BaseHTTPRequestHandler):
    def _echo(self):
        # 解析 URL：路径 + 查询参数（问号后面那串）
        parsed = urlparse(self.path)
        # 读取请求体（POST 的数据在这）
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length).decode("utf-8") if length else ""

        info = {
            "方法": self.command,                    # GET / POST / ...
            "路径": parsed.path,
            "GET参数": dict(parse_qs(parsed.query)), # URL 问号后面的参数
            "POST数据": body,                        # 请求体
            "请求头": dict(self.headers),            # 所有请求头
        }

        # 服务器终端打印（你的观察窗口）
        print("\n" + "=" * 50)
        print(json.dumps(info, ensure_ascii=False, indent=2))

        # 返回 JSON 给客户端
        resp = json.dumps(info, ensure_ascii=False).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(resp)))
        self.end_headers()
        self.wfile.write(resp)

    def do_GET(self):
        self._echo()

    def do_POST(self):
        self._echo()

    def log_message(self, *args):  # 关闭默认日志，保持输出干净
        pass

HTTPServer(("0.0.0.0", 8090), EchoHandler).serve_forever()
