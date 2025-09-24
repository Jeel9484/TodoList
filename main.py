from fastapi import FastAPI
from database import engine
from models import Base
from crud import Router as crud_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(crud_router,prefix="/todos",tags=["todos"])

@app.get("/")
def home(title:str, description : str = "This is a To-Do API", done: bool = False):
    return {"message": f"Welcome to the To-Do API, {title}!", "description": description, "done": done}
