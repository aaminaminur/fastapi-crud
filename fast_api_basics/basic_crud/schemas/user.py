from pydantic import BaseModel


class User(BaseModel):
    name: str
    phone: int
    is_test: bool
