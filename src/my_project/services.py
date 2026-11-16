from fastapi import status
from fastapi.exceptions import HTTPException

from my_project.models import User, UserRole, Pet
from my_project.repositories import UserRepository, PetRepository
from my_project.schemas import UserCreate, PetCreate


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.__user_repository = user_repository

    async def signup(self, user: UserCreate) -> User:
        # Проверка на уникальность
        if await self.__user_repository.get_by_email(user.email):
            raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Email already exists")
        if await self.__user_repository.get_by_login(user.login):
            raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Login already exists")

        all_users = await self.__user_repository.get_all()
        role = UserRole.ADMIN if len(all_users) == 0 else UserRole.USER

        model = User(
            id=0,
            role=role,
            login=user.login,
            name=user.name,
            email=user.email,
            password=user.password
        )
        await self.__user_repository.save(model)
        return model
        
    async def get_by_id(self, id: int) -> User:
        model = await self.__user_repository.get_by_id(id)
        if model is None:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail="User was not found")
        return model

    async def get_all(self) -> list[User]:
        return await self.__user_repository.get_all()


class PetService:
    def __init__(self, pet_repository: PetRepository, user_repository: UserRepository):
        self.__pet_repository = pet_repository
        self.__user_repository = user_repository

    async def create(self, pet_data: PetCreate) -> Pet:
        owner = await self.__user_repository.get_by_id(pet_data.owner_id)
        if owner is None:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Owner not found")

        pet = Pet(
            id=0,
            name=pet_data.name,
            species=pet_data.species,
            age=pet_data.age,
            owner_id=pet_data.owner_id
        )
        await self.__pet_repository.save(pet)
        return pet

    async def get_all(self) -> list[Pet]:
        return await self.__pet_repository.get_all()