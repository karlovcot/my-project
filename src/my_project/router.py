from typing import Annotated

from fastapi import APIRouter, Depends, Request, status

from my_project.schemas import (
    StatusResponse,
    User,
    UserCreate,
    UserResponse,
)
from my_project.services import UserService

users_database: dict[str, User]() = {} # type: ignore

VID_LIST = ["собакен","попугай", "утконос", "котэ", "лошадка", "что-то", "черепахен", "женщина"]

router = APIRouter()

def get_user_service(request: Request) -> UserService:
    return request.app.user_service

type UserServiceDep = Annotated[UserService, Depends(get_user_service)]

@router.get("/status")
def get_status() -> StatusResponse:
    return StatusResponse(status="ok")



@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(user: UserCreate, user_service: UserServiceDep):
    await user_service.signup(user)



@router.get("/users/{id}")
async def get_user_by_id(id: int, user_service: UserServiceDep) -> UserResponse:
    user = await user_service.get_by_id(id)
    return UserResponse(name= user.name, email = user.email)