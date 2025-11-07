from typing import List
from pydantic import BaseModel
from fastapi import APIRouter

#! Pydantic


class Student(BaseModel):
    id: int
    name: str
    subjects: List[str] = []


router = APIRouter(prefix="/pydantic", tags=["New", "FastAPI"])


@router.get("/")
async def test_1():
    data = {
        "id": 1,
        "name": "Rajiv Gandhi",
        "subjects": ["Phy", "Chem", "Math", "Geo", "Hist"],
    }

    return Student(**data)
