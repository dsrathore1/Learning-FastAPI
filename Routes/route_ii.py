from fastapi import APIRouter

router = APIRouter(prefix="/route2", tags=["Route 2"])

@router.get("/")
async def read_route2() -> list[str]:
    return ["This is Route 2"]
