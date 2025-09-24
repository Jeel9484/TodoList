from fastapi import APIRouter,Depends,HTTPException
from pydantic import BaseModel
from database import get_db
from sqlalchemy.orm import Session
from models import ToDo as ToDO
from typing import List,Optional

Router = APIRouter()


class ToDOCreate(BaseModel):
    title: str
    description: Optional[str] = None
    done: bool

class ToDoResponse(ToDOCreate):
    id: int

@Router.get("/",response_model=list[ToDoResponse])
def Show_Todos(db: Session = Depends(get_db)):
    return db.query(ToDO).all()

@Router.post("/",response_model=ToDoResponse)
def create_todo(todo: ToDOCreate, db: Session = Depends(get_db)):
    new_todo = ToDO(title=todo.title, description=todo.description, done=todo.done)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

@Router.put("/{todo_id}",response_model=ToDoResponse)
def update_todo(todo_id: int, updated_todo: ToDOCreate, db: Session = Depends(get_db)):
    db_todo = db.query(ToDO).filter(ToDO.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db_todo.title = updated_todo.title
    db_todo.description = updated_todo.description
    db_todo.done = updated_todo.done
    db.commit()
    db.refresh(db_todo)
    return db_todo

@Router.delete("/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = db.query(ToDO).filter(ToDO.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(db_todo)
    db.commit()
    return {"message": "Todo deleted successfully"}