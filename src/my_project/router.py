from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from my_project.schemas import StatusResponse, UserResponse, User

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
