import typing
import datetime


class TheOne:
    def __call__(self, environ: dict, start_response: typing.Callable):
        # print("当前时间:", datetime.datetime.now())
        # start_response("200 OK", [('Content-Type', 'text/plain; charset=utf-8')])
        # return [f"<h1>TheOne</h1>".encode("utf-8")]
        pass
