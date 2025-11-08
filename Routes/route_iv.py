from fastapi import APIRouter, Cookie, Response, Form

router = APIRouter(prefix="/cookies")


@router.post("/set_cookie")
async def set_cookie(response: Response):
    name = "Rajkumar"
    response.set_cookie(
        key="username",
        value=name,
        max_age=60,  #! 60 sec = 1 min
        httponly=True,  #! Not accessible from javascript
    )
    return {"message": "Cookie set!", "Set Name": name}


@router.get("/get_cookie")
async def get_cookie(username: str = Cookie(None)):
    if username:
        return {"message": f"Hello {username}"}
    return {"message": "No cookie found."}
