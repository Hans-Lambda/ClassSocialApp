from fastapi import FastAPI
from class_social.users import users_router

app = FastAPI()
app.include_router(users_router)
