from fastapi import FastAPI
from fastapi.routing import APIRoute
from fastapi.staticfiles import StaticFiles

from app.routes import api_router

app = FastAPI()

app.include_router(api_router)
app.mount("/static", StaticFiles(directory="app/static"), name="static")
