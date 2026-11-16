from typing import Annotated

from pydantic import BaseModel, EmailStr, StringConstraints


class StatusResponse(BaseModel):
    status: str


class UserResponse(BaseModel):
    name: str
    email: str

class User(BaseModel):
    login: str
    name: str
    email: str
    password: str

class UserCreate(BaseModel):
    login: Annotated[str, StringConstraints(min_length=1)]
    name: Annotated[str, StringConstraints(min_length=1)]
    email: EmailStr
    password: Annotated[str, StringConstraints(min_length=6, max_length=32)]

class Animal(BaseModel):
    name: str
    species: str
    age: int


class AnimalResponse(BaseModel):
    id: int
    name: str
    species: str
    age: int