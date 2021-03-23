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


@app.get("/i/{fjas_param}")
def fjas_funksjon(fjas_param):
    fjas_dict = {"en": 1, "to": 2, "tre": 3}

    if fjas_param in fjas_dict.keys():
        return fjas_dict[fjas_param]
    else:
        return {"message": "No valid key received."}


@app.post("/items/")
async def create_item(item: Item):
    return item
