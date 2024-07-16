from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/users/me/")
async def current_user():
    return {"user_id": "current_user"}


@app.get("/users/{user_id}")
async def get_user(user_id: str):
    """
    Get the details of user with id {user_id}
    """
    return {"user_id": user_id}


@app.get("/users/")
async def get_users():
    """
    Get list of users
    """
    return ["User1", "User2"]
