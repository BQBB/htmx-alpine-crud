from ninja import Schema


class SuccessSchema(Schema):
    message: str


class ErrorSchema(Schema):
    message: str
