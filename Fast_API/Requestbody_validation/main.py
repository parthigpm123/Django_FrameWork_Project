from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional


class Item(BaseModel):
      name : str = Field(min_length=3, max_length=50, pattern="^[a-zA-Z")
      price  : float
      available : Optional[bool] = Field(default=True, description="Availability of the item")
      
app=FastAPI()      

@app.post("/display")
def view(data : Item):
      return {"message": "Item received", "data": data}