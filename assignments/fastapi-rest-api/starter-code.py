from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

class Item(ItemCreate):
    id: int

items: List[Item] = [
    Item(id=1, name="Sample Item", description="A starter item.", price=9.99, tax=0.5)
]

@app.get("/items/", response_model=List[Item])
def read_items(q: Optional[str] = None):
    # TODO: Return the list of items, optionally filtered by query parameter
    return items

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    # TODO: Return a single item by ID
    for item in items:
        if item.id == item_id:
            return item
    return {"error": "Item not found"}

@app.post("/items/", response_model=Item)
def create_item(item: ItemCreate):
    # TODO: Create and return a new item with a unique ID
    new_item = Item(id=len(items) + 1, **item.dict())
    items.append(new_item)
    return new_item
