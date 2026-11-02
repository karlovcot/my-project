from pydantic import BaseModel


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


class Animal(BaseModel):
    name: str
    species: str
    age: int


class AnimalResponse(BaseModel):
    id: int
    name: str
    species: str
    age: int