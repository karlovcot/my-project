from enum import StrEnum

from pydantic import BaseModel

from my_project.models import UserRole


class UserRole(StrEnum):  # noqa: F811
    USER = "USER"
    ADMIN = "ADMIN"

class User(BaseModel):
    id: int
    login: str
    name: str
    role: UserRole
    email: str
    password: str