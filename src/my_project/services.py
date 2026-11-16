from fastapi import status
from fastapi.exceptions import HTTPException

from my_project.models import User, UserRoll
from my_project.repositories import UserRepository
from my_project.schemas import UserCreate


class UserService:
    def __init__(self, user_repositories: UserRepository):

        self.__user_repository = user_repositories

        async def signup(self,user: UserCreate) -> User:
            all_users = await self._user_repository.get_all()
            if len(all_users) == 0:
               roll = UserRoll.ADMIN
            else:
             roll = UserRoll.USER
            
            model = User(
             id = 0,
             roll = roll,
             login = user.login,
             name = user.name,
             email = user.email,
             password = user.password)

            await self.__user_repository.save(model)
            return model
        
        async def get_by_id(self, id: int) -> User|None :
           model = await self.__user_repository.get_by_id(id)
           if model is None:
              raise HTTPException(status.HTTP_404_NOT_FOUND, detail="User was not found")
           return model

        async def get_all(self) -> list[User]:
           return await self.__user_repository