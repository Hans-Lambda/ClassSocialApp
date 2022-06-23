from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


class User(BaseModel):

    name: str
    age: int
    email: str
    password: str


class UserController:

    def register_user(self, user):
        raise NotImplementedError()


users_router = APIRouter()
user_controller = UserController


@users_router.post('/users')
def post_user(user: User):
    result = user_controller.register_user(user)

    if result is True:
        return
    else:
        raise HTTPException(status_code=400)
