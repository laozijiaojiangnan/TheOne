import typing as t
from http.server import HTTPServer, BaseHTTPRequestHandler

from . import response as resp


class WsgiServer(HTTPServer):
    pass


class WsgiHandel(BaseHTTPRequestHandler):

    def handle(self) -> None:
        handle_response = SimpleHandler(self.wfile)
        handle_response.send()


class SimpleHandler:

    def __init__(self, wfile):
        self._response = resp.Response.create_empty()  # type: resp.Response
        self.sender = wfile

    def send(self):
        """像浏览器发送包
        node: 下面分成了三次发送，因为合在发送会有 bug，不确定问题，暂时先这样
        """
        line = f"{self._response.line.version} {self._response.line.code} {self._response.line.code}\r\n"
        self.sender.write(bytes(line, 'utf-8'))

        self.add_header(key='Content-Length', value=len(self._response.body.content))
        headers = "".join(
            [f"{h.key}:{h.value}\r\n" for h in self._response.headers]
        )
        print(f'headers: {headers}')
        self.sender.write(bytes(headers, 'utf-8'))

        body = f"\r\n{self._response.body.content}"
        self.sender.write(bytes(body, 'utf-8'))

    def add_header(self, key: str, value: t.Any) -> t.List[resp.Headers]:
        """添加请求头键值对
        Args:
            key: 键
            value: 值
        Return:
            存在的所有键值对信息
        """
        if self._response is None:
            self._response = resp.Response.create_empty()
        h = resp.Headers(key=key, value=value)
        self._response.headers.append(h)
        return self._response.headers
