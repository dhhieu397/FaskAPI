
from fastapi import FastAPI
from enum import Enum
from typing import Union


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet ="resnet"
    lenet ="lenet"

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

##QUERY PARAMS:
# fake_items = [{"item_name":"Foo"},{"item_name":"Bar","item_name":"lizz","item_name":"hh"}]
# @app.get("/items/")
# async def read_item(skip:int=0, limit:int=10):#default param
#     return fake_items[skip:skip+limit]

###Optinal params:
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None]= None):
    if q:
        return {"item_id":item_id, "q": q}
    return {"item_id": item_id}
# http://127.0.0.1:8000/items/honghieu?q=1


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
# http://127.0.0.1:8000/users/1/items/honghieu?q=1
# http://127.0.0.1:8000/users/1/items/honghieu



# @app.get("/")
# async def root():
#     return {"message":"Hello world"}
#
# #truyền param vào đường dẫn
# @app.get("/items/{item_id}")
# async def read_item(item_id):
#     return {"item_id":item_id}
#
# #truyền vào định dạng của param:
# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id":item_id}
#
# #2 path giống nhau, sẽ ưu tiên
# @app.get("/users")
# async def read_users():
#     return ["Rick", "Morty"]
#
# @app.get("/users")
# async def read_users2():
#     return ["Bean", "Elfo"]

# POST: to create data.
# GET: to read data.
# PUT: to update data.
# DELETE: to delete data.


