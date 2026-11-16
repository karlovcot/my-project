from __future__ import annotations
from my_project.models import User, Pet

class UserRepository:
    def __init__(self):
        self.__last_id = 0 
        self.__table = dict[int, User]()

    async def save(self, user: User):
        self.__last_id += 1  # Исправлено: было =+
        user.id = self.__last_id 
        self.__table[user.id] = user

    async def get_by_id(self, id: int) -> User | None:
        return self.__table.get(id)

    async def get_all(self) -> list[User]:
        return list(self.__table.values())

    # Добавлено для проверки уникальности
    async def get_by_email(self, email: str) -> User | None:
        for user in self.__table.values():
            if user.email == email:
                return user
        return None

    async def get_by_login(self, login: str) -> User | None:
        for user in self.__table.values():
            if user.login == login:
                return user
        return None


class PetRepository:
    def __init__(self):
        self.__last_id = 0
        self.__table = dict[int, Pet]()

    async def save(self, pet: Pet):
        self.__last_id += 1
        pet.id = self.__last_id
        self.__table[pet.id] = pet

    async def get_by_id(self, id: int) -> Pet | None:
        return self.__table.get(id)

    async def get_all(self) -> list[Pet]:
        return list(self.__table.values())