from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World", "hællæ": "omg", "pc_gaming": "ftw"}


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.get("/i/{fjas}")
def fjas_funksjon(fjas):
    if fjas == "en":
        return {"message": 1}
    if fjas == "to":
        return {"message": 2}
    if fjas == "tre":
        return {"message": 3}


@app.post("/items/")
async def create_item(item: Item):
    return item
