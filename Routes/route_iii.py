from pydantic import BaseModel, Field
from typing import List, Optional
from fastapi import APIRouter, Form

#! Pydantic


class Student(BaseModel):
    roll_no: int
    name: str = Field(
        ..., title="The description of this item", max_length=50
    )  #! In Pydantic, the ellipsis '...' is used to indicate that a field is required — it must be provided when creating the model.
    subjects: List[str] = Field(default_factory=list)
    isFemale: Optional[bool]


router = APIRouter(prefix="/pydantic", tags=["New", "FastAPI"])


@router.get("/")
async def test_1():
    data = {
        "roll_no": 1,
        "name": "Rajiv Gandhi",
        "subjects": ["Phy", "Chem", "Math", "Geo", "Hist"],
        "isFemale": False,
    }

    return Student(**data)  #! **data → unpacks the dictionary into keyword arguments.


@router.post("/get_info")
async def test_2(s1: Student):
    return s1


class User(BaseModel):
    username: str
    password: str


@router.post("/form_collection")
async def test_3(uname: str = Form(...), pwd: str = Form(...)):
    # return {"username": uname, "password": pwd}
    #! We can also do
    return User(username=uname, password=pwd)
