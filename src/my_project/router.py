from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from my_project.schemas import StatusResponse, UserResponse, User, Animal, AnimalResponse

router = APIRouter()

users_database = dict[str, User]()


@router.get("/status")
def get_status() -> StatusResponse:
    return StatusResponse(status="ok")


@router.post("/signup", status_code=201)
def signup(user: User):
    if user.login in users_database:
        raise HTTPException(409)
    users_database[user.login] = user


@router.get("/user/{login}")
def get_user(login: str) -> UserResponse:
    if login not in users_database:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    user = users_database[login]
    return UserResponse(
        name=user.name,
        email=user.email,
    )


animals_database: dict[int, Animal] = {}
_next_animal_id: int = 1


@router.post("/animal", status_code=201)
def create_animal(animal: Animal) -> AnimalResponse:
    global _next_animal_id
    animal_id = _next_animal_id
    _next_animal_id += 1
    animals_database[animal_id] = animal
    return AnimalResponse(
        id=animal_id,
        name=animal.name,
        species=animal.species,
        age=animal.age,
    )


@router.get("/animal")
def list_animals() -> list[AnimalResponse]:
    return [
        AnimalResponse(
            id=aid,
            name=a.name,
            species=a.species,
            age=a.age,
        )
        for aid, a in animals_database.items()
    ]


@router.get("/animal/{animal_id}")
def get_animal(animal_id: int) -> AnimalResponse:
    if animal_id not in animals_database:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    a = animals_database[animal_id]
    return AnimalResponse(
        id=animal_id,
        name=a.name,
        species=a.species,
        age=a.age,
    )