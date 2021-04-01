from typing import Optional

from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Query, Path
from enum import Enum

from configs import app_config

app = FastAPI(**app_config)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:*",
        "http://127.0.0.1:*",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.post("/items/{item_id}")
async def create_item(
        item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),
        item: Optional[Item] = None,
        size: float = Query(..., gt=0, lt=10.5)
):
    result = {"item_id": item_id, "size": size, **item.dict()}
    return result


@app.get("/items/")
async def read_items(
        q: Optional[str] = Query(
            None,  # if want required, use ...
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
        )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
