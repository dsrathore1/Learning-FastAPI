from fastapi import FastAPI

app = FastAPI()


#! Root Path
@app.get("/")
async def root():
    return {"message": "Hello Genius"}


#! Path parameter - Integer
@app.get("/items/{item_id}")
async def readItem(item_id: int):
    return {"Item ID ": item_id}


#! Path parameter - String
@app.get("/items_name/{item_name}")
async def readItemName(item_name: str):
    return {"Item Name ": item_name}

#! Query Parameters