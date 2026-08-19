# SSE 演示服务器：模拟 LLM 一个字一个字地"流式"回复
# 访问 http://localhost:8091/chat 时，服务器不停推送，连接不断开
from http.server import HTTPServer, BaseHTTPRequestHandler
import time

class SSEHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # SSE 的关键：响应头声明这是"事件流"
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")  # ← SSE 的标志
        self.send_header("Cache-Control", "no-cache")          # 不缓存
        self.send_header("Connection", "keep-alive")           # 保持连接
        self.end_headers()

        # 模拟 LLM 逐字生成
        reply = "你好，我是AI助手！"
        for char in reply:
            # SSE 消息格式：data: <内容>\n\n
            self.wfile.write(f"data: {char}\n\n".encode("utf-8"))
            self.wfile.flush()          # 立刻推出去，不等缓冲
            time.sleep(0.3)             # 模拟生成耗时（打字机节奏）

        # 结束事件
        self.wfile.write(b"data: [DONE]\n\n")
        self.wfile.flush()

    def log_message(self, *args):
        pass

HTTPServer(("0.0.0.0", 8091), SSEHandler).serve_forever()
