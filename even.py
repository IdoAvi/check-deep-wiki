from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Define a Pydantic model for POST request body
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "query": q}

@app.post("/items/")
def create_item(item: Item):
    return {"message": "Item created successfully", "item": item}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

