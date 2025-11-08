from fastapi import FastAPI
from Routes import route_i, route_ii, route_iii, route_iv

app = FastAPI()

app.include_router(route_i.router)
app.include_router(route_ii.router)
app.include_router(route_iii.router)
app.include_router(route_iv.router)


@app.get("/")
async def read_root() -> str:
    return "Hello, World!"
