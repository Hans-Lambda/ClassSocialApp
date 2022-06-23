from fastapi import FastAPI
from class_social.users import users_router
import uvicorn

app = FastAPI()
app.include_router(users_router)

if __name__ == '__main__':

    uvicorn.run(app='class_social.main:app', reload=True, host='127.0.0.1', port=8001)
