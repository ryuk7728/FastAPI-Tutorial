from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel): 
    text: str = None, 
    is_done: bool # If the default value is not present, then its compulsory to pass in

items = []

@app.get("/")
def root():
    return {"message":"Welcome to the todo list API!"}


@app.get("/items", response_model=list[Item])
def get_limit_items(limit:int=10):
    return items[:limit]

@app.post("/items")
def create_item(item:Item):
    items.append(item)
    return items


@app.delete("/items/delete")
def delete_item(item:Item):
    if item in items:
        items.remove(item)
        return f"Item {item} deleted successfully, updated items: {items}"
    else:
        return f"Item {item} not found"


@app.get("/items/{item_id}") #If I specify the item_id in the path, it will be passed as a path parameter to the function and i can use the link as http://127.0.0.1:8000/items/1 instead of http://127.0.0.1:8000/items?item_id=1
def get_item_byID(item_id:int):
    if item_id<0 or item_id>=len(items):
        return HTTPException(status_code=404,detail=f"Item {item_id} not found")
    else:
        item = items[item_id]
        return item