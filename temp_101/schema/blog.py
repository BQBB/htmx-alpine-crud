from ninja import Schema


class BlogSchema(Schema):
    id: int
    title: str
    description: str


class BlogIn(Schema):
    title: str
    description: str
