from sqlmodel import SQLModel, Field
from typing import Optional


#! Create Model
class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    completed: bool = False