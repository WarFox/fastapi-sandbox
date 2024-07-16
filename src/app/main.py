from enum import Enum
from typing import Annotated

from fastapi import Body, FastAPI, Path, Query
from pydantic import BaseModel, Field, HttpUrl


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float | None = None
    tags: set[str] = set()
    images: list[Image] | None = None


class Image(BaseModel):
    url: HttpUrl
    name: str


class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]


class User(BaseModel):
    username: str
    full_name: str | None = None


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer


@app.get("/items/{item_id}/")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the time to get")],
    q: Annotated[
        str,
        None,
        Query(
            alias="item-query",
            title="Query String",
            description="Query string for the items to search in database",
            min_length=3,
        ),
    ] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@app.put("/items/{item_id}")
async def update_item(
    item_id: int, item: Item, user: User, importance: Annotated[int, Body()]
):
    results = {"item_id": item_id, "item": item, "user": user, importance: importance}
    return results


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
