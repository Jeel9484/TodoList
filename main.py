from fastapi import FastAPI
from database import engine
from models import Base
from crud import Router as crud_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

Base.metadata.create_all(bind=engine)

import os

# Allow all origins in production, localhost for development
allowed_origins = ["*"] if os.getenv("ENVIRONMENT") == "production" else ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(crud_router,prefix="/todos",tags=["todos"])

@app.get("/")
def home(title:str, description : str = "This is a To-Do API", done: bool = False):
    return {"message": f"Welcome to the To-Do API, {title}!", "description": description, "done": done}
