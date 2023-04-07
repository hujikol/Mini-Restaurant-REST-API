from fastapi import FastAPI
from routers.main_routers import router

app = FastAPI()

app.include_router(router)
