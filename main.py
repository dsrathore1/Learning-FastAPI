from fastapi import FastAPI

app = FastAPI()



@app.get("/")
async def read_root() -> str:
    return "Hello, World!"
