from fastapi import APIRouter

router = APIRouter()

@router.get("/userDetails")
async def get_item():
    items = [{"name": "Alok Kumar", "age": 24}, {"name": "Rajesh Khanna", "age": 30}]
    return items
