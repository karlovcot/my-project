from fastapi import FastAPI

from my_project.router import router
from my_project.repositories import UserRepository, PetRepository
from my_project.services import UserService, PetService

app = FastAPI()

user_repository = UserRepository()
pet_repository = PetRepository()

app.user_service = UserService(user_repository)
app.pet_service = PetService(pet_repository, user_repository)

app.include_router(router)