"""wsgi web 服务器"""
import typing as t

from http.server import BaseHTTPRequestHandler, HTTPServer


class WsgiHandler(BaseHTTPRequestHandler):
    pass


class WsgiServer(HTTPServer):

    def __init__(
        self,
        address: t.Tuple[str, int] = ("127.0.0.1", 5000),
        handler_class: t.ClassVar[WsgiHandler] = WsgiHandler
    ) -> None:
        super(WsgiServer, self).__init__(address, handler_class)

    def serve_forever(self, poll_interval: float = 0.5) -> None:
        """
        :param poll_interval: 轮询时间，检查 socket 事件是否就绪
        :return:
        """
        super(WsgiServer, self).serve_forever(poll_interval)
