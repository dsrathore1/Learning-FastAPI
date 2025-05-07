from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from database import create_db_and_table, engine
from models import Todo
from sqlmodel import Session, select
from typing import List
import logging

#! Setup basic logging
logging.basicConfig(level=logging.INFO)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("🚀 Starting up... Creating database tables.")
    create_db_and_table()

    yield

    #! Shutdown login (cleanup)
    logging.info("🛑 Shutting down... Cleaning up resources")


app = FastAPI(lifespan=lifespan)

#! Root path
@app.get("/")
def root_page():
    return {"message": "Hello Genius"}

#! Create Todo list
@app.post("/todo/", response_model=Todo)
def create_todo(todo: Todo):
    with Session(engine) as session:
        session.add(todo)
        session.commit()
        session.refresh(todo)
        return todo


#! Get all todos
@app.get("/todo/", response_model=List[Todo])
def get_all_todos():
    with Session(engine) as session:
        todos = session.exec(select(Todo)).all()
        return todos


#! Get todo by id
@app.get("/todo/{todo_id}/", response_model=Todo)
def get_todo(todo_id: int):
    with Session(engine) as session:
        todo = session.get(Todo, todo_id)
        if not todo:
            raise HTTPException(status_code=404, detail="Todo not found")
        return todo
