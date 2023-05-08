from ninja import Schema
from pydantic import Field


class SuccessResponse(Schema):
    success: bool = False


class ErrorResponse(Schema):
    error: str = "Error"


class NotFoundResponse(Schema):
    message: str = "Not found"


class NotFoundException(Exception):
    def __init__(self, name: str = "Object", id: str = "ID"):
        self.name = name
        self.id = id
