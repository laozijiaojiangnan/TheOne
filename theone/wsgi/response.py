import abc
import typing
from dataclasses import dataclass


class ResponseAbstract(abc.ABC):

    @abc.abstractmethod
    def create_empty(cls):
        raise NotImplementedError


@dataclass
class Line(ResponseAbstract):
    version: str
    code: int
    message: str

    @classmethod
    def create_empty(cls):
        return cls(
            version="HTTP/1.0",
            code=200,
            message="OK"
        )


@dataclass
class Headers(ResponseAbstract):
    key: str
    value: str

    @classmethod
    def create_empty(cls):
        return cls(
            key="Content-Type",
            value="text/plain; charset=utf-8"
        )


@dataclass
class Body(ResponseAbstract):
    content: str

    @classmethod
    def create_empty(cls):
        return cls(
            content="hello theone"
        )


@dataclass
class Response(ResponseAbstract):
    line: Line
    headers: typing.List[Headers]
    body: Body

    @classmethod
    def create_empty(cls):
        return cls(
            line=Line.create_empty(),
            headers=[Headers.create_empty()],
            body=Body.create_empty()
        )
