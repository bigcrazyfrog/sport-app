from ninja import Schema
from pydantic import Field


class SuccessResponse(Schema):
    success: bool = False


class ErrorResponse(Schema):
    error: str = "Error"


class NotFoundResponse(Schema):
    message: str = "Not found"
