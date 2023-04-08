from fastapi import FastAPI
from app.api import main

app = FastAPI()

app.include_router(main.router)
