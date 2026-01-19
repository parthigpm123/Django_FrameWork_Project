from pydantic import BaseModel

class User(BaseModel):
      name: str
      age: int
      city: str
u=User(name="Alice", age=30, city="New York")
print(u.dict())      