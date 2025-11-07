from fastapi import APIRouter

router = APIRouter(prefix="/route1", tags=["Route 1"])


@router.get("/")
async def read_route1() -> dict[str, str]:
    return {"message": "This is Route 1"}
