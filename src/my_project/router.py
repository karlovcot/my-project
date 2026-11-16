from typing import Annotated
from fastapi import APIRouter, Depends, Request, status

from my_project.schemas import (
    StatusResponse,
    UserCreate,
    UserResponse,
    PetCreate,
    PetResponse,
)
from my_project.services import UserService, PetService

router = APIRouter()

def get_user_service(request: Request) -> UserService:
    return request.app.user_service

def get_pet_service(request: Request) -> PetService:
    return request.app.pet_service

type UserServiceDep = Annotated[UserService, Depends(get_user_service)]
type PetServiceDep = Annotated[PetService, Depends(get_pet_service)]


@router.get("/status")
def get_status() -> StatusResponse:
    return StatusResponse(status="ok")


@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(user: UserCreate, user_service: UserServiceDep):
    await user_service.signup(user)


@router.get("/users/{id}")
async def get_user_by_id(id: int, user_service: UserServiceDep) -> UserResponse:
    user = await user_service.get_by_id(id)
    return UserResponse(name=user.name, email=user.email)


@router.get("/users", response_model=list[UserResponse])
async def get_all_users(user_service: UserServiceDep):
    return await user_service.get_all()


@router.post("/pets", status_code=status.HTTP_201_CREATED)
async def create_pet(pet: PetCreate, pet_service: PetServiceDep):
    await pet_service.create(pet)


@router.get("/pets", response_model=list[PetResponse])
async def get_all_pets(pet_service: PetServiceDep):
    return await pet_service.get_all()