from fastapi import APIRouter


users_router = APIRouter()

@users_router.post('/users')
def post_user(user: User):
    user_controller.register_user(user)
