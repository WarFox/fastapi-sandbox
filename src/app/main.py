from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


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


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
